from behave import *
import allure
import time
from helper.RegistrationOfUserForEFilling import RegistrationOfUserForEFilling
from helper.ServiceManagerOperator import ServiceManagerOperator

sm = ServiceManagerOperator().StartServiceManager()

@given('Service Manager Dashboard')
def step_impl(context):
  allure.step("Service Manager is successfully opened")
  time.sleep(8)
  pass
    

@then('Select Work Items to navigate to Classify Case')
def step_impl(context):
  RegistrationOfUserForEFilling().NavigateToClassifyCase(sm)


@when('Classify Case pane open click Authenticate Client')
def step_impl(context):
  RegistrationOfUserForEFilling().NavigateToClassifyClient(sm)


@then('Navigate to search client')
def step_then(context):
  RegistrationOfUserForEFilling().OpenSearchClientForm(sm)


@when('Search client form opens, capture client information')
def step_when(context):
   RegistrationOfUserForEFilling().TypeUserInformation(sm)


@then('Search for the client to see if they exist and the add client')
def step_then(context):
  RegistrationOfUserForEFilling().SearchForUser(sm)
  RegistrationOfUserForEFilling().AddUserAsNewUser(sm)
