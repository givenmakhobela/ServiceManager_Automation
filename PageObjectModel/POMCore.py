from pywinauto import mouse
from pywinauto import keyboard

class POMCore:
  def __init__(self, context):
    # Constructor
    self.context = context
  
  def DoubleClickWithMouse(self):
    rect = self.context.rectangle()
    x, y = rect.mid_point()

    mouse.double_click(button='left', coords=(x, y))
  
  def ClickWithMouse(self):
    rect = self.context.rectangle()
    x, y = rect.mid_point()

    mouse.double_click(button='left', coords=(x, y))

  def ClickWorkFlowDone(self):
    keyboard.send_keys('{F5}')
  
  def SelectAllText(self):
    keyboard.send_keys('^a')
  
  def TypeText(self, text):
    keyboard.send_keys(text)
  
  def doesElementExist(self, text=None, xpath=None):
    # Todo
    return
  
  def scrollToElement(self, text=None, xpath=None, direction=None, totalNumberOfSwipes=20):
    # Todo
    return
  
  def scrollUp(self, text=None, xpath=None):
    # Todo
    return
  
  def scrollDown(self, text=None, xpath=None):
    # Todo
    return