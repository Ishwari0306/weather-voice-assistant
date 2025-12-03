# Quick Reference - Weather Voice Assistant

## 🚀 Quick Start (3 Commands)

```bash
# 1. Install
pip install -r requirements.txt

# 2. Configure (edit .env with your API key)
copy .env.example .env

# 3. Run
python app.py
```

Then open: http://localhost:5000

---

## 📋 Command Reference

### Setup Commands
```bash
# Automated setup (Windows)
setup.bat

# Automated setup (Linux/Mac)
chmod +x setup.sh
./setup.sh

# Manual setup
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
```

### Testing Commands
```bash
# Test setup
python test_setup.py

# Test weather API directly
python weather_api.py
```

### Running the Application
```bash
# Browser demo (easiest)
python app.py

# LiveKit agent (full voice agent)
python agent.py dev

# With custom port
set FLASK_PORT=8000  # Windows
export FLASK_PORT=8000  # Linux/Mac
python app.py
```

---

## 🔑 API Keys

### OpenWeatherMap (Required)
1. Sign up: https://openweathermap.org/api
2. Get key: https://home.openweathermap.org/api_keys
3. Add to `.env`: `OPENWEATHER_API_KEY=your_key_here`

### OpenAI (Optional - for LiveKit)
1. Sign up: https://platform.openai.com/signup
2. Get key: https://platform.openai.com/api-keys
3. Add to `.env`: `OPENAI_API_KEY=sk-your_key_here`

---

## 💬 Example Queries

### Current Weather
```
✓ "What's the weather in Mumbai?"
✓ "Weather in Delhi"
✓ "How's the weather in Bangalore?"
✓ "Temperature in Chennai"
✓ "Tell me about the weather in Kolkata"
```

### Forecast
```
✓ "Will it rain in Pune tomorrow?"
✓ "Tomorrow's weather in Hyderabad"
✓ "Forecast for Jaipur"
✓ "What will the weather be like in Goa tomorrow?"
```

### Error Testing
```
✓ "Weather in XYZ123"          # Invalid city
✓ "Tell me about it"            # No city mentioned
```

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `app.py` | Browser demo (Flask app) |
| `agent.py` | LiveKit voice agent |
| `weather_api.py` | Weather API integration |
| `test_setup.py` | Verify setup |
| `.env` | API keys (create from .env.example) |
| `README.md` | Full documentation |

---

## 🐛 Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "API key not found"
1. Create `.env` file (copy from `.env.example`)
2. Add your actual API key
3. Save the file

### "Port already in use"
Change port in `.env`:
```env
FLASK_PORT=8000
```

### Voice not working in browser
- Use Chrome or Edge
- Allow microphone permissions
- Use HTTPS or localhost

### "City not found"
- Check spelling
- Use English names
- Try major cities first

---

## 🎥 Demo Recording Checklist

### Before Recording
- [ ] Test the app works
- [ ] Close unnecessary windows
- [ ] Prepare test queries
- [ ] Check microphone works

### What to Show (2-3 min)
1. [ ] Open app (http://localhost:5000)
2. [ ] Voice query: "What's the weather in Mumbai?"
3. [ ] Text query: "Weather in Bangalore"
4. [ ] Forecast: "Will it rain in Pune tomorrow?"
5. [ ] Error: "Weather in XYZ123"

### Tools
- Windows: Xbox Game Bar (Win + G)
- Cross-platform: OBS Studio
- Web-based: Loom

---

## 📦 Project Structure

```
new_pro/
├── app.py                 # Main demo app
├── agent.py               # LiveKit agent
├── weather_api.py         # API integration
├── test_setup.py          # Tests
├── requirements.txt       # Dependencies
├── .env                   # Your API keys
├── README.md              # Documentation
└── templates/
    └── index.html         # Web interface
```

---

## ✅ Submission Checklist

### Code
- [ ] All files in repository
- [ ] Clean, commented code
- [ ] No API keys in code (use .env.example)
- [ ] .gitignore configured

### Documentation
- [ ] README.md complete
- [ ] Setup instructions clear
- [ ] Comments in code

### Demo
- [ ] 2-3 minute video recorded
- [ ] Shows voice input
- [ ] Shows text input
- [ ] Shows error handling

### Repository
- [ ] GitHub repository public
- [ ] All files committed
- [ ] Clear repository name
- [ ] README as homepage

---

## 🔗 Useful Links

- OpenWeatherMap API: https://openweathermap.org/api
- LiveKit Docs: https://docs.livekit.io/agents/
- OpenAI API: https://platform.openai.com/docs
- Flask Docs: https://flask.palletsprojects.com/

---

## 💡 Pro Tips

1. **Test early**: Run `test_setup.py` before starting
2. **Start simple**: Use browser demo first
3. **Check logs**: Look for error messages
4. **Use examples**: Copy exact queries from docs
5. **Stay calm**: Most issues are config problems

---

## 📞 Common Issues

| Issue | Solution |
|-------|----------|
| Import errors | `pip install -r requirements.txt` |
| API key error | Check `.env` file exists and has correct key |
| Port in use | Change `FLASK_PORT` in `.env` |
| Voice not working | Use Chrome/Edge, check mic permissions |
| API rate limit | Wait a few seconds between requests |

---

**Need more help?** See `SETUP_GUIDE.md` for detailed instructions.

**Ready to start?** Run: `python app.py`
