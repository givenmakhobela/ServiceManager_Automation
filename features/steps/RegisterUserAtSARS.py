from behave import *
import allure
import time
from helper.RegistrationOfUserAtSARS import RegistrationOfUserAtSARS
from helper.ServiceManagerOperator import ServiceManagerOperator

sm = ServiceManagerOperator().StartServiceManager()

@given('Service Manager Dashboard')
def step_impl(context):
  allure.step("Service Manager is successfully opened")
  time.sleep(8)
  pass
    

@then('Select Work Items to navigate to Classify Case')
def step_impl(context):
  RegistrationOfUserAtSARS().NavigateToClassifyCase(sm)


@when('Classify Case pane open click Authenticate Client')
def step_impl(context):
  RegistrationOfUserAtSARS().NavigateToClassifyClient(sm)


@then('Navigate to search client')
def step_then(context):
  RegistrationOfUserAtSARS().OpenSearchClientForm(sm)


@when('Search client form opens, capture client information')
def step_when(context):
   RegistrationOfUserAtSARS().TypeUserInformation(sm)


@then('Search for the client to see if they exist and the add client')
def step_then(context):
  RegistrationOfUserAtSARS().SearchForUser(sm)
  RegistrationOfUserAtSARS().AddUserAsNewUser(sm)

@given('Entity Registration form apply xml data')
def step_given(context):
    RegistrationOfUserAtSARS().ApplyXMLDataToForm(sm)

@then('Click Done button')
def step_then(context):
    RegistrationOfUserAtSARS().SubmitByClickingDone(sm)