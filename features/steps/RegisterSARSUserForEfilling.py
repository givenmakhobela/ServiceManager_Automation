from behave import *
import allure
import time
from helper.RegistrationOfUserAtSARS import RegistrationOfUserAtSARS
from helper.ServiceManagerOperator import ServiceManagerOperator
from helper.RegisterSARSUserForEfilling import RegisterSARSUserForEfilling

sm = ServiceManagerOperator().StartServiceManager()


@given(u'Service Manager Dashboard - efilling')
def step_impl(context):
  allure.step("Service Manager is successfully opened")
  time.sleep(8)
  pass


@then(u'Select Work Items to navigate to Classify Case - efilling')
def step_impl(context):
  RegistrationOfUserAtSARS().NavigateToClassifyCase(sm)


@when(u'Classify Case pane open click Authenticate Client - efilling')
def step_impl(context):
  RegistrationOfUserAtSARS().NavigateToClassifyClient(sm)


@then(u'Navigate to search client - efilling')
def step_impl(context):
  RegistrationOfUserAtSARS().OpenSearchClientForm(sm)


@when(u'Search client form opens, capture client information - efilling')
def step_impl(context):
  RegisterSARSUserForEfilling().TypeUserInformation(sm)


@then(u'Search for the registered client and select the client - efilling')
def step_impl(context):
  RegistrationOfUserAtSARS().SearchForUser(sm)


@then(u'Perform eFilling registration service - efilling')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Perform eFilling registration service - efilling')