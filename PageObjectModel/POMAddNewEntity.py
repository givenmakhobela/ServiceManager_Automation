from pywinauto import keyboard
from PageObjectModel.POMCore import POMCore
from Utilities.allure import AllureStep
from pywinauto.timings import wait_until

class POMAddNewEntity:
  def __init__(self, instance):
    self.instance = instance
  
  def ClickAddNew(self):
    try:

      wait_until(60, 1, lambda: self.instance["Add New Entity"].child_window(title="_Add", control_type="Text").exists(), True)
      
      element = self.instance["Add New Entity"].child_window(title="_Add", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))