"""
Configuration file for Weather Voice Assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # OpenWeatherMap API
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    # OpenAI API (for LiveKit agent)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LiveKit Configuration
    LIVEKIT_URL = os.getenv("LIVEKIT_URL", "ws://localhost:7880")
    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY", "devkey")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET", "secret")
    
    # Flask Configuration
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        errors = []
        
        if not cls.OPENWEATHER_API_KEY or cls.OPENWEATHER_API_KEY == "your_api_key_here":
            errors.append("OPENWEATHER_API_KEY is not set in .env file")
        
        if errors:
            raise ValueError(f"Configuration errors:\n" + "\n".join(f"- {e}" for e in errors))
        
        return True


# Weather API settings
WEATHER_API_TIMEOUT = 10  # seconds
WEATHER_UNITS = "metric"  # Use Celsius

# Assistant personality settings
ASSISTANT_NAME = "Weather Bot"
ASSISTANT_GREETING = "Hello! I'm your weather assistant. Ask me about the weather in any city!"
