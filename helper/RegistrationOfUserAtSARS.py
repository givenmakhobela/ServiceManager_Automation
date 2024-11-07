import allure
from time import sleep
from PageObjectModel.POMServiceNavigation import POMServiceNavigation
from PageObjectModel.POMClassifyCase import POMClassifyCase
from PageObjectModel.POMSearchClient import POMSearchClient
from PageObjectModel.POMAuthenticateClient import POMAuthenticateClient
from PageObjectModel.POMPane import POMPane
from PageObjectModel.POMCore import POMCore
from PageObjectModel.POMAddNewEntity import POMAddNewEntity
from Utilities.DataSourceUtil import DataSourceUtil
from Utilities.allure import AllureStep, AllureScreenshot


class RegistrationOfUserAtSARS:

  def __init__(self):
    self.sleepTimeout = 1
    self.name = None
    self.surname = None
    self.dateOfBirth = None
    self.passportNumber = None
    self.entityRegistration = None
  
  def NavigateToClassifyCase(self, context):
    AllureStep('Click Work Items from Navigation')
    POMServiceNavigation().ClickWorkItem(context, 'Work Items')
    AllureScreenshot(context)

    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)

    AllureStep('Select Classify case')
    POMServiceNavigation().ClickMenuRow(context, 0)
    AllureScreenshot(context)
    pass
  
  def NavigateToClassifyClient(self, context):
    AllureStep('Click Authenticate client')
    POMClassifyCase().ClickItem(context, 0)
    AllureScreenshot(context)

    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    
    AllureStep('Close the alert dialog presented after success message')
    POMClassifyCase().OnCaseCreatedClickOkay(context)
    AllureScreenshot(context)
    pass

  def OpenSearchClientForm(self, context):
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)

    AllureStep('Clicking Search button')
    AllureScreenshot(context)
    POMAuthenticateClient.SearchButton(context)
    AllureScreenshot(context)  

  def GetUserData(self):
    personalInformation = DataSourceUtil().GetUnregisteredUser()
    
    self.name = personalInformation[1]
    self.surname = personalInformation[2]
    self.dateOfBirth = personalInformation[3]
    self.passportNumber = personalInformation[4]

    self.entityRegistration = DataSourceUtil().GetEntityRegistrationXML().replace('_name_', self.name).replace('_surname_', self.surname).replace('_dateofbirth_', self.dateOfBirth.replace('/', '-')).replace('__passport__', self.passportNumber)
  
  def TypeUserInformation(self, context):
    self.GetUserData()
    
    AllureStep(f'Typing date of birth {self.dateOfBirth}')
    POMSearchClient(context).TypeDateofBirth(self.dateOfBirth)
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing first name {self.name}')
    POMSearchClient(context).TypeFirstName(self.name)
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing first surname {self.surname}')
    POMSearchClient(context).TypeSurname(self.surname)
    AllureStep(f'Selecting passport as an option')
    POMSearchClient(context).SelectPassport()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing passport number no {self.passportNumber}')
    POMSearchClient(context).TypeIdentificationNo(self.passportNumber)
    AllureScreenshot(context)
  
  def SearchForUser(self, context):
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep('Maximizing window')
    POMSearchClient(context).MaximizeWindow()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep('Searching for client to check if they exist')
    POMSearchClient(context).SearchForClient()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureScreenshot(context)
    AllureStep('Closing dialog with anticipation that they do not exist')
    POMSearchClient(context).CloseAlertDialog()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
  
  def AddUserAsNewUser(self, context):
    AllureStep('Accepting SARS terms before adding new user')
    POMSearchClient(context).AcceptBothTerms()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep('Adding new user')
    AllureScreenshot(context)
    POMSearchClient(context).ClickNew()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep('Click add on entity registration dialog')
    AllureScreenshot(context)
    POMAddNewEntity(context).ClickAddNew()
  
  def ApplyXMLDataToForm(self, context):
    self.GetUserData()
    
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureScreenshot(context)
    AllureStep('Click Entity Registration Pane')
    POMPane().ClickPaneXMLEditor(context)
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    ##### Submitting the default xml because the template one I have prevents the user from successfully getting approved.
    ##AllureStep('Select all text')
    ##AllureScreenshot(context)
    ##POMCore(context).SelectAllText()
    ##sleep(self.sleepTimeout)
    ##AllureStep(f'Type xml data for the registration: {self.entityRegistration}')
    #POMCore(context).TypeText(self.entityRegistration)
    AllureScreenshot(context)
  
  def SubmitByClickingDone(self, context):
    AllureStep('Click done after typing typing the xml')
    POMCore(context).ClickWorkFlowDone()
    AllureScreenshot(context)
    sleep(self.sleepTimeout)
    AllureStep('Click done to confirm changes')
    POMCore(context).ClickWorkFlowDone()
    AllureScreenshot(context)
    AllureStep('Pop registered user from unregistered users to registered users CSV file')
    DataSourceUtil().AddUnregisteredUserToRegisteredUsersFile()





