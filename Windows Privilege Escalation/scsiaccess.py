import servicemanager
import win32serviceutil
import win32service
import win32api

import os
import ctypes

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'

    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)

    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)

    def SvcDoRun(self):

        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            self.start()

        except:
            self.SvcStop()
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPEED)

    def start(self):
        self.runflag=True
        '''
        f = open('C:/Users/nonadmin/Desktop/priv.txt', 'w')
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            f.write('[-] We are NOT admin')
        else:
            f.write('[+] We are admin')
        f.close()
        '''
    def stop(self):
        self.runflag=False

if __name__ == '__main__':


    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service)

