#!/bin/bash
# Setup script for Weather Voice Assistant (Linux/Mac)

echo "============================================================"
echo "Weather Voice Assistant - Automated Setup"
echo "============================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/5] Python found!"
echo

# Create virtual environment
echo "[2/5] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    echo "Virtual environment created!"
fi
echo

# Activate virtual environment and install dependencies
echo "[3/5] Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo

# Create .env file if it doesn't exist
echo "[4/5] Setting up environment file..."
if [ -f ".env" ]; then
    echo ".env file already exists, skipping..."
else
    cp .env.example .env
    echo ".env file created! Please edit it with your API keys."
fi
echo

# Run tests
echo "[5/5] Running setup tests..."
python test_setup.py
echo

echo "============================================================"
echo "Setup Complete!"
echo "============================================================"
echo
echo "Next steps:"
echo "1. Edit .env file and add your OpenWeatherMap API key"
echo "2. Run: python app.py"
echo "3. Open browser to: http://localhost:5000"
echo
echo "See SETUP_GUIDE.md for detailed instructions!"
echo
