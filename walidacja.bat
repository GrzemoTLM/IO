@echo off

REM Sprawdzenie, czy Python jest zainstalowany
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python nie jest zainstalowany. Proszę zainstalować Python i spróbować ponownie.
    pause
    exit /b 1
)

REM Uruchomienie skryptu walidacji
python3 walidacja.py

pause
