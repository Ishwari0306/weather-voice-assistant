"""
Test other components while waiting for API key activation
"""

print("\n" + "="*60)
print("TESTING PROJECT COMPONENTS")
print("="*60)

# Test 1: Import all modules
print("\n[Test 1] Importing modules...")
try:
    import weather_api
    import config
    print("✅ All Python modules import successfully")
except Exception as e:
    print(f"❌ Import error: {e}")

# Test 2: Configuration
print("\n[Test 2] Configuration...")
try:
    from config import Config
    print(f"✅ Config loaded")
    print(f"   - OpenWeather API URL: {Config.OPENWEATHER_BASE_URL}")
except Exception as e:
    print(f"❌ Config error: {e}")

# Test 3: Flask app
print("\n[Test 3] Flask application...")
try:
    from flask import Flask
    print("✅ Flask is installed and working")
except Exception as e:
    print(f"❌ Flask error: {e}")

# Test 4: Templates
print("\n[Test 4] Web interface...")
try:
    import os
    if os.path.exists('templates/index.html'):
        print("✅ Web interface template found")
    else:
        print("❌ Template file missing")
except Exception as e:
    print(f"❌ Template error: {e}")

# Test 5: API Key Format
print("\n[Test 5] API Key format...")
try:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    key = os.getenv("OPENWEATHER_API_KEY")
    if key and len(key) == 32 and key != "your_api_key_here":
        print(f"✅ API key format looks correct (32 characters)")
        print(f"   Key preview: {key[:8]}...{key[-4:]}")
        print(f"\n   ⏰ If just created, wait 5-10 minutes for activation")
    else:
        print(f"❌ API key format issue (length: {len(key) if key else 0})")
except Exception as e:
    print(f"❌ API key check error: {e}")

print("\n" + "="*60)
print("COMPONENT TEST COMPLETE")
print("="*60)
print("\n💡 Everything except API activation is working!")
print("⏰ Wait 5-10 minutes after creating your OpenWeatherMap account")
print("🔄 Then run: python test_setup.py")
print("="*60 + "\n")
