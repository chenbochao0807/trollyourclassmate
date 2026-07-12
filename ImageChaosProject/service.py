import win32serviceutil
import win32service
import win32event
import servicemanager
import subprocess
import time
import os

class ImageChaosService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ImageChaosService"
    _svc_display_name_ = "Image Chaos Service"
    _svc_description_ = "Runs chaos_script.py periodically to display images."

    def __init__(self, args):
        super().__init__(args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ""))
        self.main()

    def main(self):
        while self.running:
            try:
                subprocess.Popen(["python", "chaos_script.py"], cwd=os.path.dirname(__file__))
            except Exception as e:
                error_path = os.path.join(os.path.dirname(__file__), 'service_error.txt')
                with open(error_path, "a") as f:
                    f.write(f"{time.ctime()} - Error: {e}\n")
            time.sleep(60) 

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ImageChaosService)
