ImageChaos Installer

This package installs the ImageChaos application on Windows machines.

Requirements:
- Windows 10/11
- Python 3.x installed and in PATH

Installation:
1. Extract the ZIP file to a folder.
2. Run install.bat as administrator.
3. The installer will:
   - Install required Python packages (pywin32, Pillow)
   - Copy files to C:\ProgramData\ImageChaos
   - Set up auto-start on login
   - Hide files for persistence
   - Start the daemon

The application will display random images on screen every 60 seconds, starting automatically on login.

To uninstall: Delete C:\ProgramData\ImageChaos and remove from startup folder.