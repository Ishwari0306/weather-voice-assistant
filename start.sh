#!/bin/bash
# Quick Start Script - Weather Voice Assistant
# This script helps you quickly start the application

echo ""
echo "============================================================"
echo "   Weather Voice Assistant - Quick Start"
echo "============================================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[ERROR] Virtual environment not found!"
    echo ""
    echo "Please run setup.sh first:"
    echo "   chmod +x setup.sh"
    echo "   ./setup.sh"
    echo ""
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "[WARNING] .env file not found!"
    echo ""
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "[IMPORTANT] Please edit .env and add your API keys!"
    echo ""
    echo "1. Open .env in a text editor"
    echo "2. Add your OpenWeatherMap API key"
    echo "3. Save the file"
    echo "4. Run this script again"
    echo ""
    exit 1
fi

# Activate virtual environment
echo "[1/3] Activating virtual environment..."
source venv/bin/activate
echo ""

# Check if dependencies are installed
python -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[2/3] Installing dependencies..."
    pip install -q -r requirements.txt
    echo "Dependencies installed!"
else
    echo "[2/3] Dependencies already installed"
fi
echo ""

# Start the application
echo "[3/3] Starting Weather Voice Assistant..."
echo ""
echo "============================================================"
echo ""
echo "The application is starting!"
echo ""
echo "Once it's running, open your browser and go to:"
echo "   http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "============================================================"
echo ""

python app.py
