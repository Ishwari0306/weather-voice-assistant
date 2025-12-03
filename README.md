# 🌤️ Weather Voice Assistant

A voice-enabled weather assistant built with LiveKit Agents Framework and OpenWeatherMap API. Ask about weather conditions in any city using voice or text input!

## 📋 Project Overview

This project was created for the **Vaiu AI Software Developer Internship Assignment**. It demonstrates:

- ✅ Voice agent integration with custom API functions
- ✅ Real-time weather data fetching
- ✅ Natural language processing for weather queries
- ✅ Error handling and user-friendly responses
- ✅ Clean, documented code structure

## 🎯 Features

- **Voice Input**: Speak naturally to ask about weather
- **Voice Output**: Get spoken responses from the assistant
- **Current Weather**: Ask about current conditions in any city
- **Weather Forecast**: Get tomorrow's weather predictions
- **Rain Probability**: Find out chances of rain
- **Error Handling**: Graceful handling of invalid cities and API errors

## 🛠️ Technology Stack

- **Voice Framework**: LiveKit Agents (with fallback to Web Speech API)
- **Weather API**: OpenWeatherMap
- **Language Model**: OpenAI GPT-4o-mini
- **Speech-to-Text**: OpenAI Whisper
- **Text-to-Speech**: OpenAI TTS
- **Web Framework**: Flask (for browser demo)
- **Language**: Python 3.8+

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenWeatherMap API key (free tier available)
- OpenAI API key (for voice features)

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd new_pro
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Keys

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Get your **OpenWeatherMap API Key**:
   - Visit: https://openweathermap.org/api
   - Sign up for free account
   - Generate API key
   - Copy key to `.env` file

3. Get your **OpenAI API Key** (for voice features):
   - Visit: https://platform.openai.com/api-keys
   - Create API key
   - Copy key to `.env` file

4. Update `.env` file:
   ```env
   OPENWEATHER_API_KEY=your_actual_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🚀 Usage

### Option 1: Browser-Based Demo (Recommended for Quick Testing)

The easiest way to test the weather assistant:

```bash
python app.py
```

Then open your browser and go to:
```
http://localhost:5000
```

**Features:**
- Click "Start Voice" to speak your query
- Or type in the text box and click "Send"
- Get both text and voice responses
- Works in Chrome, Edge, and modern browsers

**Example Queries:**
- "What's the weather in Mumbai?"
- "How about Bangalore?"
- "Will it rain in Pune tomorrow?"

### Option 2: LiveKit Agent (Production Voice Agent)

For full voice agent capabilities with LiveKit:

1. **Install LiveKit CLI**:
   ```bash
   pip install livekit-cli
   ```

2. **Start LiveKit Server** (in a new terminal):
   ```bash
   livekit-server --dev
   ```

3. **Run the Agent** (in another terminal):
   ```bash
   python agent.py dev
   ```

4. **Connect via LiveKit Playground**:
   - Open: http://localhost:7880
   - Join a room
   - Start speaking!

### Option 3: Test Weather API Directly

To test just the weather API integration:

```bash
python weather_api.py
```

This will run test queries for Mumbai, Bangalore, and an invalid city.

## 📁 Project Structure

```
new_pro/
├── agent.py              # Main LiveKit voice agent
├── app.py                # Flask web application for browser demo
├── weather_api.py        # Weather API integration module
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── templates/
    └── index.html       # Web interface for browser demo
```

## 🔧 Configuration

### Weather API Settings

Edit `config.py` to customize:

```python
WEATHER_API_TIMEOUT = 10  # API request timeout in seconds
WEATHER_UNITS = "metric"  # Temperature units (metric = Celsius)
ASSISTANT_NAME = "Weather Bot"
```

### LiveKit Settings

For production deployment, update `.env`:

```env
LIVEKIT_URL=wss://your-livekit-server.com
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_secret
```

## 🧪 Testing

### Manual Testing

Run the test script:
```bash
python weather_api.py
```

### Interactive Testing

1. Start the browser demo: `python app.py`
2. Try these queries:
   - Current weather: "What's the weather in Delhi?"
   - Forecast: "Will it rain in Chennai tomorrow?"
   - Multiple cities: "Weather in Mumbai" then "How about Bangalore?"

### Error Handling Tests

- Invalid city: "Weather in XYZ123"
- Ambiguous query: "Tell me the weather"
- Network issues: (disconnect internet and try)

## 📸 Demo Recording

To create your demo recording:

1. Start the application: `python app.py`
2. Use screen recording software (Windows: Xbox Game Bar, OBS)
3. Demonstrate these scenarios:
   - Voice query for current weather
   - Text query for forecast
   - Error handling with invalid city
4. Keep recording under 3 minutes

## 🐛 Troubleshooting

### "API key not found" error

**Solution**: Make sure you've copied `.env.example` to `.env` and added your actual API keys.

### "Module not found" errors

**Solution**: 
```bash
pip install -r requirements.txt
```

### Voice recognition not working in browser

**Solution**: 
- Use Chrome or Edge browser
- Allow microphone permissions
- Ensure HTTPS or localhost

### "City not found" error

**Solution**: 
- Check spelling of city name
- Try major cities: Mumbai, Delhi, Bangalore
- Use English city names

### LiveKit connection issues

**Solution**:
- Ensure LiveKit server is running: `livekit-server --dev`
- Check if port 7880 is available
- Verify LIVEKIT_URL in `.env`

## 🔐 API Keys & Rate Limits

### OpenWeatherMap Free Tier
- 1,000 calls per day
- 60 calls per minute
- Current weather + 5-day forecast

### OpenAI Free Tier
- $5 free credit for new accounts
- GPT-4o-mini: Very cost-effective
- Whisper STT: $0.006/minute
- TTS: $15/1M characters

## 🚀 Deployment Options

### Local Development
✅ Current setup - perfect for testing and demo

### Cloud Deployment
- **Heroku**: Easy deployment with web dyno
- **AWS/GCP/Azure**: Full control and scalability
- **Vercel/Netlify**: For static frontend with serverless backend

### LiveKit Cloud
- Use LiveKit Cloud for production voice agent
- Update `.env` with cloud credentials

## 📚 Learning Resources

- **LiveKit Docs**: https://docs.livekit.io/agents/
- **OpenWeatherMap API**: https://openweathermap.org/api
- **OpenAI API**: https://platform.openai.com/docs
- **Flask**: https://flask.palletsprojects.com/

## 🎓 Assignment Checklist

✅ **Core Requirements**
- [x] Voice input/output functionality
- [x] Custom weather API function
- [x] Extract city from user speech
- [x] Fetch real-time weather data
- [x] Natural voice responses
- [x] Error handling (city not found, API failures, unclear input)

✅ **Deliverables**
- [x] Working voice agent (browser demo + LiveKit agent)
- [x] Weather API integration
- [x] Clean code with comments
- [x] README with setup instructions
- [ ] 2-3 min screen recording (you need to create this)

## 👨‍💻 Code Quality

- **Clean Structure**: Modular design with separate concerns
- **Documentation**: Comprehensive comments and docstrings
- **Error Handling**: Try-catch blocks and user-friendly messages
- **Type Hints**: Clear function signatures
- **Best Practices**: Following Python and LiveKit conventions

## 📝 License

This project is created for educational purposes as part of an internship assignment.

## 🤝 Contributing

This is an assignment project, but suggestions are welcome!

## 📧 Contact

For questions about this project, please reach out through your internship coordinator.

---

**Built with ❤️ for Vaiu AI Internship Assignment**

## 🎉 Quick Start Summary

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up API keys in .env
copy .env.example .env
# Edit .env with your API keys

# 3. Run browser demo
python app.py

# 4. Open browser
# Go to http://localhost:5000

# 5. Start talking!
# Click "Start Voice" and ask: "What's the weather in Mumbai?"
```

Enjoy your weather assistant! 🌦️
