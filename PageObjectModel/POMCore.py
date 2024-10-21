from pywinauto import mouse

class POMCore:
  def __init__(self, context):
    # Constructor
    self.context = context
  
  def DoubleClickWithMouse(self):
    rect = self.context.rectangle()
    x, y = rect.mid_point()

    mouse.double_click(button='left', coords=(x, y))

  def clickElement(self, text=None, xpath=None):
    # Todo
    return
  
  def waitForElement(self, text=None, xpath=None, timeout=5):
    # Todo
    return
  
  def pause(self, text=None, xpath=None, timeout=0):
    # Todo
    return
  
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