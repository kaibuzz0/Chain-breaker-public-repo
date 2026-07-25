@echo off
echo ============================================
echo   CHAIN-BREAKER INSTALLER
echo ============================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found! Please install from:
    echo https://python.org/downloads
    echo.
    echo IMPORTANT: Check "Add Python to PATH"
    pause
    exit /b 1
)

echo [OK] Python found

REM Install from appropriate repo
echo.
echo Installing Chain-Breaker...
echo.

REM Try private repo first, fall back to public
git clone https://github.com/kaibuzz0/chain-breaker.git temp 2>nul
if errorlevel 1 (
    echo Installing from public repository...
    git clone https://github.com/kaibuzz0/Chain-breaker-public-repo.git chain-breaker
) else (
    echo Installing from private repository...
    rename temp chain-breaker
)

cd chain-breaker
pip install -r requirements.txt

echo.
echo ============================================
echo   INSTALLATION COMPLETE!
echo ============================================
echo.
echo To use:
echo   cd chain-breaker
echo   python vault_cli.py --list
echo.
pause
