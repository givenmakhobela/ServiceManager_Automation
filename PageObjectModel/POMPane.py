from Utilities.allure import AllureStep
from time import sleep
from PageObjectModel.POMCore import POMCore
from pywinauto.timings import wait_until

class POMPane:
  def ClickPaneXMLEditor(self, instance):
    try:

      wait_until(60, 1, lambda: instance.window(auto_id="Main").child_window(title="txtXmlData", auto_id="txtXmlData", control_type="Edit").exists(), True)

      element  = instance.window(auto_id="Main").child_window(title="txtXmlData", auto_id="txtXmlData", control_type="Edit")

      POMCore(element).ClickWithMouse()

      return True
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))