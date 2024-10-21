import psutil
from pywinauto.application import Application


class ServiceManagerOperator:

  def GetApplicationProcess(self):
    applicationName = "ServiceManager.exe"

    for runningProcesses in psutil.process_iter(['pid', 'name']):
      if runningProcesses.info['name'] == applicationName:
        return runningProcesses.info['pid']
    
    return 0
  
  def StartServiceManager(self):
    processId = self.GetApplicationProcess()

    if processId == 0:
      raise Exception("Please start service manager and login in with the prefered user before running this TestCase")
    
    return Application(backend="uia").connect(process=processId)
