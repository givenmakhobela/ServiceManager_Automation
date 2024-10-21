import allure
from time import sleep
from PageObjectModel.POMServiceNavigation import POMServiceNavigation
from PageObjectModel.POMClassifyCase import POMClassifyCase


class RegistrationOfUserForEFilling:

  def __init__(self):
    self.sleepTimeout = 4
  
  @allure.step('Navigate to Classify Case')
  def NavigateToClassifyCase(self, context):
    allure.step('Click Work Items from Navigation')
    POMServiceNavigation().ClickWorkItem(context, 'Work Items')

    allure.step(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)

    allure.step('Select Classify case')
    POMServiceNavigation().ClickMenuRow(context, 0)
    pass
  
  @allure.step('Authenticate ')
  def NavigateToClassifyClient(self, context):
    allure.step('Click Authenticate client')
    POMClassifyCase().ClickItem(context, 0)

    allure.step(f'sleep({self.sleepTimeout})')
    sleep(self.sleepTimeout)
    
    allure.step('Close the alert dialog presented after success message')
    POMClassifyCase().OnCaseCreatedClickOkay(context)
    pass