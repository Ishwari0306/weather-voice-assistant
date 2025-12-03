"""
Weather API Integration Module
Fetches real-time weather data from OpenWeatherMap API
"""

import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherAPI:
    """Handles weather data fetching from OpenWeatherMap"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        
        if not self.api_key or self.api_key == "your_api_key_here":
            raise ValueError(
                "OpenWeatherMap API key not found. "
                "Please set OPENWEATHER_API_KEY in .env file"
            )
    
    def get_current_weather(self, city: str) -> Dict:
        """
        Fetch current weather for a given city
        
        Args:
            city: Name of the city
            
        Returns:
            Dictionary with weather information
        """
        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"  # Use Celsius
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            # Handle HTTP errors
            if response.status_code == 404:
                return {
                    "success": False,
                    "error": "city_not_found",
                    "message": f"Sorry, I couldn't find weather data for {city}. Please check the city name."
                }
            elif response.status_code == 401:
                return {
                    "success": False,
                    "error": "api_key_invalid",
                    "message": "API authentication failed. Please check your API key."
                }
            elif response.status_code != 200:
                return {
                    "success": False,
                    "error": "api_error",
                    "message": f"Weather service returned an error: {response.status_code}"
                }
            
            data = response.json()
            
            # Extract relevant weather information
            weather_info = {
                "success": True,
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": round(data["main"]["temp"]),
                "feels_like": round(data["main"]["feels_like"]),
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "main_weather": data["weather"][0]["main"]
            }
            
            return weather_info
            
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "error": "timeout",
                "message": "Weather service request timed out. Please try again."
            }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "error": "connection_error",
                "message": "Unable to connect to weather service. Please check your internet connection."
            }
        except Exception as e:
            return {
                "success": False,
                "error": "unknown",
                "message": f"An unexpected error occurred: {str(e)}"
            }
    
    def get_forecast(self, city: str) -> Dict:
        """
        Fetch weather forecast for a given city
        
        Args:
            city: Name of the city
            
        Returns:
            Dictionary with forecast information
        """
        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric",
                "cnt": 8  # Get next 24 hours (8 x 3-hour intervals)
            }
            
            response = requests.get(self.forecast_url, params=params, timeout=10)
            
            if response.status_code == 404:
                return {
                    "success": False,
                    "error": "city_not_found",
                    "message": f"Sorry, I couldn't find forecast data for {city}."
                }
            elif response.status_code != 200:
                return {
                    "success": False,
                    "error": "api_error",
                    "message": f"Weather service returned an error: {response.status_code}"
                }
            
            data = response.json()
            
            # Get tomorrow's forecast (next day's average)
            forecasts = data["list"]
            tomorrow_data = forecasts[4:8] if len(forecasts) >= 8 else forecasts  # 12-24 hours ahead
            
            # Calculate averages for tomorrow
            avg_temp = sum(f["main"]["temp"] for f in tomorrow_data) / len(tomorrow_data)
            descriptions = [f["weather"][0]["description"] for f in tomorrow_data]
            most_common_desc = max(set(descriptions), key=descriptions.count)
            
            # Check for rain probability
            rain_chance = 0
            for forecast in tomorrow_data:
                if "rain" in forecast:
                    rain_chance = max(rain_chance, forecast.get("pop", 0) * 100)
            
            forecast_info = {
                "success": True,
                "city": data["city"]["name"],
                "country": data["city"]["country"],
                "temperature": round(avg_temp),
                "description": most_common_desc,
                "rain_probability": round(rain_chance)
            }
            
            return forecast_info
            
        except Exception as e:
            return {
                "success": False,
                "error": "unknown",
                "message": f"An unexpected error occurred: {str(e)}"
            }


def format_weather_response(weather_data: Dict) -> str:
    """
    Format weather data into a natural language response
    
    Args:
        weather_data: Dictionary containing weather information
        
    Returns:
        Natural language string describing the weather
    """
    if not weather_data["success"]:
        return weather_data["message"]
    
    city = weather_data["city"]
    temp = weather_data["temperature"]
    description = weather_data["description"]
    
    # Create natural response
    response = f"The weather in {city} is {temp}°C and {description}."
    
    # Add additional context
    if "feels_like" in weather_data:
        feels_like = weather_data["feels_like"]
        if abs(feels_like - temp) > 3:
            response += f" It feels like {feels_like}°C."
    
    if "humidity" in weather_data and weather_data["humidity"] > 80:
        response += " It's quite humid."
    
    return response


def format_forecast_response(forecast_data: Dict) -> str:
    """
    Format forecast data into a natural language response
    
    Args:
        forecast_data: Dictionary containing forecast information
        
    Returns:
        Natural language string describing the forecast
    """
    if not forecast_data["success"]:
        return forecast_data["message"]
    
    city = forecast_data["city"]
    temp = forecast_data["temperature"]
    description = forecast_data["description"]
    rain_prob = forecast_data["rain_probability"]
    
    response = f"Tomorrow in {city}, it's expected to be {temp}°C with {description}."
    
    if rain_prob > 50:
        response += f" There's a {rain_prob}% chance of rain."
    elif rain_prob > 30:
        response += f" There's a slight chance of rain at {rain_prob}%."
    
    return response


# Test function
if __name__ == "__main__":
    # Test the weather API
    weather_api = WeatherAPI()
    
    # Test current weather
    print("Testing current weather for Mumbai...")
    result = weather_api.get_current_weather("Mumbai")
    print(format_weather_response(result))
    print()
    
    # Test forecast
    print("Testing forecast for Bangalore...")
    forecast = weather_api.get_forecast("Bangalore")
    print(format_forecast_response(forecast))
    print()
    
    # Test error handling
    print("Testing error handling with invalid city...")
    error_result = weather_api.get_current_weather("InvalidCityName123")
    print(format_weather_response(error_result))
