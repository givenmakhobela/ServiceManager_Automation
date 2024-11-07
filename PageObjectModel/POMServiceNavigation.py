from PageObjectModel.POMCore import POMCore
from Utilities.allure import AllureStep
from pywinauto.timings import wait_until

class POMServiceNavigation:
  
  def ClickWorkItem(self, instance, workItemTitle):
    
    try:
      element = instance.window(auto_id='Main').child_window(title=workItemTitle)
      
      element.draw_outline()
      element.click()
      return True
    except:
      pass
    
    try:
        if instance.window(auto_id='Main').child_window(title=workItemTitle).exists() == True:
          return True
        else:
          return False
    except:
      return False
  
  def ClickMenuRow(self, instance, rowNumber=0):
    title = f'Node{rowNumber}'

    try:

      wait_until(60, 1, lambda: instance.window(auto_id='Main').child_window(title="Data Panel", control_type="Group").child_window(title="Node0", control_type="TreeItem").exists(), True)

      element = instance.window(auto_id='Main').child_window(title="Data Panel", control_type="Group").child_window(title="Node0", control_type="TreeItem")

      element.draw_outline()

      POMCore(element).DoubleClickWithMouse()
      return True
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
    
