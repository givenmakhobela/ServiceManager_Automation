from time import sleep
from pywinauto import keyboard
from PageObjectModel.POMCore import POMCore
from Utilities.allure import AllureStep
from pywinauto.timings import wait_until

class POMSearchClient:
  def __init__(self, instance):
    self.instance = instance

  def TypeDateofBirth(self, value):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="Date Of Birth", control_type="Custom").exists(), True)

      element = self.instance["Search Client"].child_window(title="Date Of Birth", control_type="Custom")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
      sleep(1)
      keyboard.send_keys(value)
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def TypeSurname(self, value):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="Surname", control_type="Text").exists(), True)

      element = self.instance["Search Client"].child_window(title="Surname", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
      sleep(1)
      keyboard.send_keys(value)
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def TypeFirstName(self, value):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="First Name", control_type="Text").exists(), True)

      element = self.instance["Search Client"].child_window(title="First Name", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
      sleep(1)
      keyboard.send_keys(value)
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))

  def SelectPassport(self):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="Passport", control_type="Text").exists(), True)

      element = self.instance["Search Client"].child_window(title="Passport", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def TypeIdentificationNo(self, value):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="ID or Passport", control_type="Text").exists(), True)

      element = self.instance["Search Client"].child_window(title="ID or Passport", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
      sleep(1)
      keyboard.send_keys(value)
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def SearchForClient(self):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="Search", control_type="Button").exists(), True)

      element = self.instance["Search Client"].child_window(title="Search", control_type="Button")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def MaximizeWindow(self):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="Maximize", control_type="Button").exists(), True)

      element = self.instance["Search Client"].child_window(title="Maximize", control_type="Button")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def CloseAlertDialog(self):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="Service Manager", control_type="Window").child_window(title="Close", control_type="Button").exists(), True)

      element = self.instance["Search Client"].child_window(title="Service Manager", control_type="Window").child_window(title="Close", control_type="Button")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def AcceptBothTerms(self):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="I have confirmed the security answers?", control_type="RadioButton").child_window(title="Yes", control_type="Text").exists(), True)

      element = self.instance["Search Client"].child_window(title="I have confirmed the security answers?", control_type="RadioButton").child_window(title="Yes", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
      sleep(1)

      element = self.instance["Search Client"].child_window(title="I have verified the ID/ Passport/ Drivers License?", control_type="RadioButton").child_window(title="Yes", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def ClickNew(self):
    try:

      wait_until(60, 1, lambda: self.instance["Search Client"].child_window(title="_New", control_type="Text").exists(), True)

      element = self.instance["Search Client"].child_window(title="_New", control_type="Text")

      element.draw_outline()
      POMCore(element).ClickWithMouse()
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))