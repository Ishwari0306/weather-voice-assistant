@echo off
REM Setup script for Weather Voice Assistant (Windows)

echo ============================================================
echo Weather Voice Assistant - Automated Setup
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo [1/5] Python found!
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv venv
    echo Virtual environment created!
)
echo.

REM Activate virtual environment and install dependencies
echo [3/5] Installing dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo.

REM Create .env file if it doesn't exist
echo [4/5] Setting up environment file...
if exist .env (
    echo .env file already exists, skipping...
) else (
    copy .env.example .env
    echo .env file created! Please edit it with your API keys.
)
echo.

REM Run tests
echo [5/5] Running setup tests...
python test_setup.py
echo.

echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Next steps:
echo 1. Edit .env file and add your OpenWeatherMap API key
echo 2. Run: python app.py
echo 3. Open browser to: http://localhost:5000
echo.
echo See SETUP_GUIDE.md for detailed instructions!
echo.
pause
