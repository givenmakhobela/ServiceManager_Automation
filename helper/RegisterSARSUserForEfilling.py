from Utilities.allure import AllureStep, AllureScreenshot
from PageObjectModel.POMSearchClient import POMSearchClient
from Utilities.DataSourceUtil import DataSourceUtil
from time import sleep

class RegisterSARSUserForEfilling:
  def __init__(self):
    self.sleepTimeout = 1
    self.passportNumber = None
  
  def GetUserData(self):
    self.passportNumber = DataSourceUtil().GetRegisteredUser()[4]

  
  def TypeUserInformation(self, context):
    self.GetUserData()
    
    AllureStep(f'Selecting passport as an option')
    POMSearchClient(context).SelectPassport()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing passport number no {self.passportNumber}')
    POMSearchClient(context).TypeIdentificationNo(self.passportNumber)
    AllureScreenshot(context)
