# Weather Voice Assistant

A voice-enabled weather assistant that provides real-time weather information for any city. Built with LiveKit Agents Framework, Flask, and OpenWeatherMap API.

## Demo Video

🎥 **Watch the demo:** [https://youtu.be/kQ22u8FCE1U](https://youtu.be/kQ22u8FCE1U)

## Features

- Voice input and output for natural interaction
- Current weather conditions for any city
- Weather forecasts and rain probability
- Text input as alternative to voice
- Error handling for invalid queries
- Modern, responsive web interface

## Technology Stack

- **Backend**: Python, Flask
- **Voice Framework**: LiveKit Agents
- **Weather API**: OpenWeatherMap
- **AI Models**: OpenAI GPT-4o-mini, Whisper (STT), TTS
- **Frontend**: HTML, CSS, JavaScript (Web Speech API)

## Installation

### Prerequisites

- Python 3.8+
- OpenWeatherMap API key ([Get free key](https://openweathermap.org/api))
- OpenAI API key (optional, for LiveKit agent)

### Setup

1. Clone the repository
```bash
git clone https://github.com/Ishwari0306/weather-voice-assistant.git
cd weather-voice-assistant
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
```
Edit `.env` and add your API keys:
```
OPENWEATHER_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here  # Optional
```

## Usage

### Browser Demo

Start the Flask application:
```bash
python app.py
```

Open http://localhost:5000 in your browser.

**Try these queries:**
- "What's the weather in Mumbai?"
- "Will it rain tomorrow in Pune?"
- "How's the weather in Bangalore?"

### LiveKit Agent

For production voice agent:
```bash
livekit-server --dev  # In one terminal
python agent.py dev    # In another terminal
```

## Project Structure

```
├── agent.py           # LiveKit voice agent
├── app.py             # Flask web application
├── weather_api.py     # Weather API integration
├── config.py          # Configuration
├── requirements.txt   # Dependencies
├── .env.example       # Environment template
└── templates/
    └── index.html     # Web interface
```

## Testing

Run the test script to verify setup:
```bash
python test_setup.py
```

Test the weather API directly:
```bash
python weather_api.py
```

## Troubleshooting

**API key error**: Ensure `.env` file exists with valid API keys  
**Module not found**: Run `pip install -r requirements.txt`  
**Voice not working**: Use Chrome/Edge, allow microphone access  
**City not found**: Check spelling, use English city names

## License

MIT License

---

Built for Vaiu AI Software Developer Internship Assignment
