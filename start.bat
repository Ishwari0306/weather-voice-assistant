@echo off
REM Quick Start Script - Weather Voice Assistant
REM This script helps you quickly start the application

echo.
echo ============================================================
echo    Weather Voice Assistant - Quick Start
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist venv (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run setup.bat first:
    echo    setup.bat
    echo.
    pause
    exit /b 1
)

REM Check if .env exists
if not exist .env (
    echo [WARNING] .env file not found!
    echo.
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo [IMPORTANT] Please edit .env and add your API keys!
    echo.
    echo 1. Open .env in a text editor
    echo 2. Add your OpenWeatherMap API key
    echo 3. Save the file
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Check if dependencies are installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [2/3] Installing dependencies...
    pip install -q -r requirements.txt
    echo Dependencies installed!
) else (
    echo [2/3] Dependencies already installed
)
echo.

REM Start the application
echo [3/3] Starting Weather Voice Assistant...
echo.
echo ============================================================
echo.
echo The application is starting!
echo.
echo Once it's running, open your browser and go to:
echo    http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ============================================================
echo.

python app.py
