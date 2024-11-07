from Utilities.allure import AllureStep
from pywinauto.timings import wait_until
class POMAuthenticateClient:

  def SearchButton(instance):

    try:
      wait_until(60, 1, lambda: instance.window(auto_id="Main").child_window(best_match ="Entity Registration Authenticate Client", control_type="TabItem").exists(), True)
      wait_until(60, 1, lambda: instance.window(auto_id='Main').child_window(title="Search", control_type="Button").exists(), True)

      element = instance.window(auto_id='Main').child_window(title="Search", control_type="Button")
      
      element.draw_outline()
      element.click()

      return True
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))