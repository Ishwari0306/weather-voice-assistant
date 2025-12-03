"""
Simple Weather Voice Assistant Demo (Browser-based)
Uses Web Speech API for simpler testing without LiveKit server
"""

import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from weather_api import WeatherAPI, format_weather_response, format_forecast_response

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize weather API
weather_api = WeatherAPI()


@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')


@app.route('/api/weather', methods=['POST'])
def get_weather():
    """API endpoint to get weather information"""
    data = request.json
    query = data.get('query', '').lower()
    
    # Enhanced intent detection
    # Check for tomorrow/forecast queries (explicit future)
    tomorrow_keywords = ['tomorrow', 'forecast', 'next day']
    is_tomorrow_query = any(keyword in query for keyword in tomorrow_keywords)
    
    # Check for rain queries without "tomorrow" - should check forecast
    rain_query_without_tomorrow = ('rain' in query or 'raining' in query) and not any(word in query for word in ['today', 'now', 'current', 'currently'])
    
    if is_tomorrow_query or (rain_query_without_tomorrow and 'tomorrow' not in query):
        # Get forecast for tomorrow
        city = extract_city(query)
        if city:
            forecast_data = weather_api.get_forecast(city)
            response = format_forecast_response(forecast_data)
            return jsonify({'response': response, 'success': forecast_data['success']})
    else:
        # Get current weather (for today, now, or general weather questions)
        city = extract_city(query)
        if city:
            weather_data = weather_api.get_current_weather(city)
            
            # If asking about rain today, mention rain probability from current data
            if 'rain' in query and 'today' in query:
                if weather_data['success']:
                    weather_desc = weather_data['description'].lower()
                    if 'rain' in weather_desc or 'drizzle' in weather_desc:
                        response = f"Yes, it's currently raining in {weather_data['city']}. The weather is {weather_data['description']} with a temperature of {weather_data['temperature']}°C."
                    else:
                        response = f"No, it's not raining in {weather_data['city']} right now. The weather is {weather_data['description']} with a temperature of {weather_data['temperature']}°C."
                else:
                    response = format_weather_response(weather_data)
            else:
                response = format_weather_response(weather_data)
            
            return jsonify({'response': response, 'success': weather_data['success']})
    
    return jsonify({
        'response': "I'm sorry, I couldn't understand which city you're asking about. Please try again.",
        'success': False
    })


def extract_city(query: str) -> str:
    """
    Enhanced city extraction from query
    
    Args:
        query: User's query string
        
    Returns:
        Extracted city name or empty string
    """
    query_lower = query.lower()
    
    # Remove common words and weather-related adjectives
    words_to_remove = [
        'what', 'is', 'the', 'weather', 'in', 'at', 'for', 'about',
        'how', 'will', 'it', 'rain', 'tomorrow', 'today', 'forecast',
        'temperature', 'like', 'whats', "what's", 'tell', 'me', 'please',
        'be', 'there', 'a', 'chance', 'of', 'going', 'to',
        # Weather condition words to remove
        'cold', 'hot', 'warm', 'cool', 'sunny', 'rainy', 'cloudy',
        'humid', 'dry', 'windy', 'foggy', 'snowy', 'stormy', 'wet'
    ]
    
    # Try to find city after "in" or "at" preposition (most common pattern)
    for prep in [' in ', ' at ']:
        if prep in query_lower:
            after_prep = query_lower.split(prep)[-1]
            # Take words after preposition, stopping at common question words
            city_part = after_prep.split('today')[0].split('tomorrow')[0].split('?')[0]
            city = city_part.strip()
            if city:
                return city.title()
    
    # Fallback: remove common words
    words = query_lower.split()
    city_words = [w for w in words if w not in words_to_remove and w.strip('?.,!')]
    
    # Join remaining words as city name
    city = ' '.join(city_words).strip()
    
    # Capitalize first letter of each word
    return city.title() if city else ""


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("=" * 60)
    print("Weather Voice Assistant Demo Starting...")
    print("=" * 60)
    print("\nOpen your browser and navigate to:")
    print("http://localhost:5000")
    print("\nMake sure you have set your OPENWEATHER_API_KEY in .env file!")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
