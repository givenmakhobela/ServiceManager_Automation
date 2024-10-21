from PageObjectModel.POMCore import POMCore

class POMClassifyCase:
  
  def ClickItem(self, instance, rowNumber):

    try:
      element = instance.window(auto_id='Main').child_window(title='Classifications').child_window(title='Bbd.Sars.CMWorkflow.ClassifyCaseWPF.Classification', found_index=0)

      POMCore(element).DoubleClickWithMouse()
      return True
    except:
      return False
  
  def OnCaseCreatedClickOkay(self, instance):

    instance.window(auto_id='Main').child_window(title="Create Case", control_type="Window").child_window(title="OK", control_type="Button").click()
    try:
      instance.window(auto_id='Main').child_window(title="Create Case", control_type="Window").child_window(title="OK").click()

      return True
    except:
      return False