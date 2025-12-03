"""
Weather Voice Assistant - LiveKit Agent
A voice-enabled assistant that provides weather information
"""

import asyncio
import logging
import os
from typing import Annotated
from dotenv import load_dotenv

from livekit import rtc
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
    llm,
)
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

from weather_api import WeatherAPI, format_weather_response, format_forecast_response

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize weather API
weather_api = WeatherAPI()


class WeatherAssistantFunctions(llm.FunctionContext):
    """Weather assistant function definitions for LLM"""
    
    @llm.ai_callable(
        description="Get the current weather for a specific city. "
        "Use this when user asks about current weather, temperature, or conditions."
    )
    async def get_weather(
        self,
        city: Annotated[str, llm.TypeInfo(description="The name of the city to get weather for")]
    ) -> str:
        """
        Fetch current weather for a city
        
        Args:
            city: Name of the city
            
        Returns:
            Formatted weather information
        """
        logger.info(f"Fetching weather for city: {city}")
        
        # Get weather data
        weather_data = weather_api.get_current_weather(city)
        
        # Format response
        response = format_weather_response(weather_data)
        
        logger.info(f"Weather response: {response}")
        return response
    
    @llm.ai_callable(
        description="Get weather forecast for tomorrow for a specific city. "
        "Use this when user asks about tomorrow's weather, future weather, or rain probability."
    )
    async def get_forecast(
        self,
        city: Annotated[str, llm.TypeInfo(description="The name of the city to get forecast for")]
    ) -> str:
        """
        Fetch weather forecast for a city
        
        Args:
            city: Name of the city
            
        Returns:
            Formatted forecast information
        """
        logger.info(f"Fetching forecast for city: {city}")
        
        # Get forecast data
        forecast_data = weather_api.get_forecast(city)
        
        # Format response
        response = format_forecast_response(forecast_data)
        
        logger.info(f"Forecast response: {response}")
        return response


async def entrypoint(ctx: JobContext):
    """
    Main entry point for the voice assistant agent
    
    Args:
        ctx: JobContext from LiveKit
    """
    # System prompt for the assistant
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a friendly weather assistant. Your name is Weather Bot. "
            "You help users get weather information for any city they ask about. "
            "When a user asks about weather, use the get_weather function to fetch current weather data. "
            "When they ask about tomorrow or future weather, use the get_forecast function. "
            "Always mention the city name in your response. "
            "Be conversational and helpful. "
            "If the user greets you, greet them back warmly. "
            "Keep responses concise but informative."
        ),
    )
    
    logger.info("Connecting to room: %s", ctx.room.name)
    
    # Connect to the room
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    
    # Wait for the first participant to join
    participant = await ctx.wait_for_participant()
    logger.info(f"Participant joined: {participant.identity}")
    
    # Initialize the voice assistant
    assistant = VoiceAssistant(
        vad=silero.VAD.load(),  # Voice Activity Detection
        stt=openai.STT(),  # Speech-to-Text
        llm=openai.LLM(model="gpt-4o-mini"),  # Language Model
        tts=openai.TTS(voice="alloy"),  # Text-to-Speech
        chat_ctx=initial_ctx,
        fnc_ctx=WeatherAssistantFunctions(),  # Weather functions
    )
    
    # Start the assistant
    assistant.start(ctx.room, participant)
    
    # Send initial greeting
    await assistant.say("Hello! I'm your weather assistant. Ask me about the weather in any city!", allow_interruptions=True)
    
    logger.info("Voice assistant started successfully")


async def request_fnc(req: llm.FunctionCallInfo):
    """Log function calls for debugging"""
    logger.info(f"Function called: {req.function_info.name}")
    logger.info(f"Arguments: {req.arguments}")


if __name__ == "__main__":
    # Run the agent
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            request_fnc=request_fnc,
        )
    )
