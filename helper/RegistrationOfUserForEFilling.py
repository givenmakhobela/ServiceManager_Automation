import allure
from time import sleep
from PageObjectModel.POMServiceNavigation import POMServiceNavigation
from PageObjectModel.POMClassifyCase import POMClassifyCase
from PageObjectModel.POMSearchClient import POMSearchClient
from PageObjectModel.POMAuthenticateClient import POMAuthenticateClient
from Utilities.GetDataFromDataSource import GetDataFromDataSource
from Utilities.allure import AllureStep


class RegistrationOfUserForEFilling:

  def __init__(self):
    self.sleepTimeout = 4
  
  def NavigateToClassifyCase(self, context):
    AllureStep('Click Work Items from Navigation')
    POMServiceNavigation().ClickWorkItem(context, 'Work Items')

    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)

    AllureStep('Select Classify case')
    POMServiceNavigation().ClickMenuRow(context, 0)
    pass
  
  def NavigateToClassifyClient(self, context):
    AllureStep('Click Authenticate client')
    POMClassifyCase().ClickItem(context, 0)

    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    
    AllureStep('Close the alert dialog presented after success message')
    POMClassifyCase().OnCaseCreatedClickOkay(context)
    pass

  def OpenSearchClientForm(self, context):
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)

    AllureStep('Clicking Search button')
    POMAuthenticateClient.SearchButton(context)
  
  def TypeUserInformation(self, context):
    personalInformation = GetDataFromDataSource.GetUnRegisteredUsers()
    
    name = personalInformation[1]
    surname = personalInformation[2]
    dateOfBirth = personalInformation[3]
    passportNumber = personalInformation[4]
    
    AllureStep(f'Typing date of birth {dateOfBirth}')
    POMSearchClient(context).TypeDateofBirth(dateOfBirth)
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing first name {name}')
    POMSearchClient(context).TypeFirstName(name)
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing first surname {surname}')
    POMSearchClient(context).TypeSurname(surname)
    AllureStep(f'Selecting passport as an option')
    POMSearchClient(context).SelectPassport()
    AllureStep(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    AllureStep(f'Typing passport number no {passportNumber}')
    POMSearchClient(context).TypeIdentificationNo(passportNumber)
  
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
    POMSearchClient(context).ClickNew()



