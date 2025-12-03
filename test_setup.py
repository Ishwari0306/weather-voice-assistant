"""
Test script for Weather Voice Assistant
Run this to verify your setup and API configuration
"""

import os
import sys
from dotenv import load_dotenv

def test_environment():
    """Test environment variables are set correctly"""
    print("=" * 60)
    print("TESTING ENVIRONMENT CONFIGURATION")
    print("=" * 60)
    
    load_dotenv()
    
    errors = []
    warnings = []
    
    # Check OpenWeatherMap API Key
    openweather_key = os.getenv("OPENWEATHER_API_KEY")
    if not openweather_key or openweather_key == "your_api_key_here":
        errors.append("❌ OPENWEATHER_API_KEY is not set in .env file")
    else:
        print("✅ OpenWeatherMap API Key found")
    
    # Check OpenAI API Key (optional for browser demo)
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key or openai_key == "your_openai_api_key_here":
        warnings.append("⚠️  OPENAI_API_KEY is not set (required for LiveKit agent)")
    else:
        print("✅ OpenAI API Key found")
    
    print()
    
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  {warning}")
        print()
    
    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  {error}")
        print("\n❌ Environment setup incomplete. Please fix the errors above.")
        return False
    
    print("✅ Environment configuration looks good!")
    return True


def test_weather_api():
    """Test weather API integration"""
    print("\n" + "=" * 60)
    print("TESTING WEATHER API")
    print("=" * 60)
    
    try:
        from weather_api import WeatherAPI, format_weather_response, format_forecast_response
        
        weather_api = WeatherAPI()
        print("✅ Weather API module loaded successfully\n")
        
        # Test current weather
        print("Testing current weather for Mumbai...")
        result = weather_api.get_current_weather("Mumbai")
        
        if result["success"]:
            print("✅ API call successful!")
            print(f"   Response: {format_weather_response(result)}")
        else:
            print(f"❌ API call failed: {result['message']}")
            return False
        
        print()
        
        # Test forecast
        print("Testing forecast for Bangalore...")
        forecast = weather_api.get_forecast("Bangalore")
        
        if forecast["success"]:
            print("✅ Forecast call successful!")
            print(f"   Response: {format_forecast_response(forecast)}")
        else:
            print(f"❌ Forecast call failed: {forecast['message']}")
            return False
        
        print()
        
        # Test error handling
        print("Testing error handling with invalid city...")
        error_result = weather_api.get_current_weather("InvalidCity12345XYZ")
        
        if not error_result["success"]:
            print("✅ Error handling works correctly!")
            print(f"   Response: {format_weather_response(error_result)}")
        else:
            print("⚠️  Expected an error but got success")
        
        print("\n✅ All weather API tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing weather API: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def test_dependencies():
    """Test that required packages are installed"""
    print("\n" + "=" * 60)
    print("TESTING DEPENDENCIES")
    print("=" * 60)
    
    required_packages = [
        ("requests", "API requests"),
        ("dotenv", "Environment variables"),
        ("flask", "Web application (for browser demo)"),
    ]
    
    optional_packages = [
        ("livekit", "LiveKit voice agent"),
        ("openai", "OpenAI integration"),
    ]
    
    all_good = True
    
    # Test required packages
    for package, description in required_packages:
        try:
            __import__(package)
            print(f"✅ {package:<20} - {description}")
        except ImportError:
            print(f"❌ {package:<20} - {description} [MISSING]")
            all_good = False
    
    print()
    
    # Test optional packages
    print("Optional packages (for full LiveKit agent):")
    for package, description in optional_packages:
        try:
            __import__(package)
            print(f"✅ {package:<20} - {description}")
        except ImportError:
            print(f"⚠️  {package:<20} - {description} [NOT INSTALLED]")
    
    print()
    
    if all_good:
        print("✅ All required dependencies are installed!")
    else:
        print("❌ Some required dependencies are missing.")
        print("   Run: pip install -r requirements.txt")
    
    return all_good


def main():
    """Run all tests"""
    print("\n🧪 Weather Voice Assistant - Setup Test")
    print("=" * 60)
    print("This script will verify your setup is correct.\n")
    
    # Track results
    results = {
        "dependencies": False,
        "environment": False,
        "weather_api": False
    }
    
    # Run tests
    results["dependencies"] = test_dependencies()
    
    if results["dependencies"]:
        results["environment"] = test_environment()
    else:
        print("\n⚠️  Skipping environment tests due to missing dependencies")
    
    if results["dependencies"] and results["environment"]:
        results["weather_api"] = test_weather_api()
    else:
        print("\n⚠️  Skipping weather API tests due to previous failures")
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    print(f"Dependencies:     {'✅ PASS' if results['dependencies'] else '❌ FAIL'}")
    print(f"Environment:      {'✅ PASS' if results['environment'] else '❌ FAIL'}")
    print(f"Weather API:      {'✅ PASS' if results['weather_api'] else '❌ FAIL'}")
    
    print("\n" + "=" * 60)
    
    if all(results.values()):
        print("🎉 ALL TESTS PASSED!")
        print("=" * 60)
        print("\nYour setup is complete! You can now run:")
        print("  python app.py        # Browser demo")
        print("  python agent.py dev  # LiveKit agent")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        print("=" * 60)
        print("\nPlease fix the issues above and run this test again.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
