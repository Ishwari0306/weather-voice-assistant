# Weather Voice Assistant - Setup Guide

## Quick Setup (5 minutes)

### Step 1: Get OpenWeatherMap API Key

1. Go to: https://openweathermap.org/api
2. Click "Sign Up" (top right)
3. Fill in the form:
   - Username
   - Email
   - Password
4. Verify your email
5. Go to: https://home.openweathermap.org/api_keys
6. Copy your API key (it looks like: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`)

### Step 2: Configure Your Project

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` file in a text editor

3. Replace `your_api_key_here` with your actual API key:
   ```env
   OPENWEATHER_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
   ```

4. Save the file

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Test Your Setup

```bash
python test_setup.py
```

You should see all green checkmarks (✅)!

### Step 5: Run the Demo

```bash
python app.py
```

Open your browser to: http://localhost:5000

---

## Optional: Get OpenAI API Key (for LiveKit Voice Agent)

If you want to use the full LiveKit voice agent:

1. Go to: https://platform.openai.com/signup
2. Sign up for an account
3. Go to: https://platform.openai.com/api-keys
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)
6. Add to `.env`:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   ```

Note: OpenAI gives $5 free credit to new accounts.

---

## Troubleshooting

### "API key not found" error

Make sure you:
1. Created `.env` file (not `.env.example`)
2. Added your actual API key (not the placeholder text)
3. Saved the file

### "pip: command not found"

Try:
```bash
python -m pip install -r requirements.txt
```

### Port 5000 already in use

Change the port in `.env`:
```env
FLASK_PORT=8000
```

Then access: http://localhost:8000

---

## Demo Recording Tips

1. **Prepare your screen**:
   - Close unnecessary tabs/windows
   - Set browser to a reasonable size
   - Have test queries ready

2. **What to show** (2-3 minutes total):
   - Open the app (http://localhost:5000)
   - Demonstrate voice query: "What's the weather in Mumbai?"
   - Demonstrate text query: "Weather in Bangalore"
   - Show forecast: "Will it rain in Pune tomorrow?"
   - Show error handling: "Weather in XYZ123"

3. **Recording software**:
   - Windows: Xbox Game Bar (Win + G)
   - OBS Studio (free, all platforms)
   - Screen recording in PowerPoint
   - Loom (web-based, free)

4. **Tips**:
   - Speak clearly when using voice input
   - Keep recording under 3 minutes
   - Show both voice and text input
   - Demonstrate error handling

---

## What to Submit

✅ GitHub Repository containing:
- All project files
- README.md
- Clean, commented code
- .env.example (DO NOT commit .env with real keys!)

✅ Screen Recording (2-3 minutes):
- Upload to YouTube (unlisted) or Google Drive
- Include link in README or submission form

---

## Common Test Queries

```
Current Weather:
- "What's the weather in Mumbai?"
- "Weather in Delhi"
- "How's the weather in Bangalore?"
- "Temperature in Chennai"

Forecast:
- "Will it rain in Pune tomorrow?"
- "Tomorrow's weather in Kolkata"
- "Forecast for Hyderabad"

Error Handling:
- "Weather in XYZ123" (invalid city)
- "Tell me about it" (no city mentioned)
```

---

## Need Help?

1. Run the test script: `python test_setup.py`
2. Check the troubleshooting section
3. Review error messages carefully
4. Verify API keys are correct
5. Check internet connection

---

Good luck with your assignment! 🚀
