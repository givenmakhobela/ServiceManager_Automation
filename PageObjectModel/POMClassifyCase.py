from PageObjectModel.POMCore import POMCore
from Utilities.allure import AllureStep
from pywinauto.timings import wait_until

class POMClassifyCase:
  
  def ClickItem(self, instance, rowNumber):

    try:

      wait_until(60, 1, lambda: instance.window(auto_id='Main').child_window(title='Classifications').child_window(title='Bbd.Sars.CMWorkflow.ClassifyCaseWPF.Classification', found_index=0).exists(), True)

      element = instance.window(auto_id='Main').child_window(title='Classifications').child_window(title='Bbd.Sars.CMWorkflow.ClassifyCaseWPF.Classification', found_index=0)

      element.draw_outline()

      POMCore(element).DoubleClickWithMouse()
      return True
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))
  
  def OnCaseCreatedClickOkay(self, instance):

    try:

      wait_until(60, 1, lambda: instance.window(auto_id='Main').child_window(title="Create Case", control_type="Window").child_window(title="OK").exists(), True)

      element = instance.window(auto_id='Main').child_window(title="Create Case", control_type="Window").child_window(title="OK")
      
      element.draw_outline()
      element.click()

      return True
    except Exception as e:
      AllureStep(str(e))
      raise Exception(str(e))