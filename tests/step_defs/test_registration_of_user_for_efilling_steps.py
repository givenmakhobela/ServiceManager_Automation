from pytest_bdd import scenario, given, when, then
import allure
import time
from helper.RegistrationOfUserForEFilling import RegistrationOfUserForEFilling


@scenario('../features/registration_of_user_for_efilling.feature', 'Register user for tax number')

@allure.suite("Register user for tax number")
@allure.title("Register user for tax number")
@allure.tag("Registration", "Tax number")

@allure.description("TRegister user for tax number so that they can file for efilling.")
@given('Service Manager Dashboard')
def test_step_given(context):
  allure.step("Service Manager is successfult opened")
  time.sleep(8)
  pass
    

@allure.description("Select work items to Classify Case")
@then('Select work items to Classify Case')
def test_step_then(context):
  RegistrationOfUserForEFilling().NavigateToClassifyCase(context)


@allure.description("Select work items to Classify Case")
@when('Classify Case pane open authenticate client')
def test_step_when(context):
  RegistrationOfUserForEFilling().NavigateToClassifyClient(context)