from time import sleep
from pywinauto import keyboard
from PageObjectModel.POMCore import POMCore

class POMSearchClient:
  def __init__(self, instance):
    self.instance = instance

  def TypeDateofBirth(self, value):
    element = self.instance["Search Client"].child_window(title="Date Of Birth", control_type="Custom")

    element.draw_outline()
    POMCore(element).ClickWithMouse()
    sleep(1)
    keyboard.send_keys(value)
  
  def TypeSurname(self, value):
    element = self.instance["Search Client"].child_window(title="Surname", control_type="Text")

    element.draw_outline()
    POMCore(element).ClickWithMouse()
    sleep(1)
    keyboard.send_keys(value)
  
  def TypeFirstName(self, value):
    element = self.instance["Search Client"].child_window(title="First Name", control_type="Text")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()
    sleep(1)
    keyboard.send_keys(value)

  def SelectPassport(self):
    element = self.instance["Search Client"].child_window(title="Passport", control_type="Text")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()
  
  def TypeIdentificationNo(self, value):
    element = self.instance["Search Client"].child_window(title="ID or Passport", control_type="Text")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()
    sleep(1)
    keyboard.send_keys(value)
  
  def SearchForClient(self):
    element = self.instance["Search Client"].child_window(title="Search", control_type="Button")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()
  
  def MaximizeWindow(self):
    element = self.instance["Search Client"].child_window(title="Maximize", control_type="Button")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()
  
  def CloseAlertDialog(self):
    element = self.instance["Search Client"].child_window(title="Service Manager", control_type="Window").child_window(title="Close", control_type="Button")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()
  
  def AcceptBothTerms(self):
    element = self.instance["Search Client"].child_window(title="I have confirmed the security answers?", control_type="RadioButton").child_window(title="Yes", control_type="Text")

    element.draw_outline()
    POMCore(element).ClickWithMouse()
    sleep(1)

    element = self.instance["Search Client"].child_window(title="I have verified the ID/ Passport/ Drivers License?", control_type="RadioButton").child_window(title="Yes", control_type="Text")

    element.draw_outline()
    POMCore(element).ClickWithMouse()
  
  def ClickNew(self):
    element = self.instance["Search Client"].child_window(title="_New", control_type="Text")
    
    element.draw_outline()
    POMCore(element).ClickWithMouse()