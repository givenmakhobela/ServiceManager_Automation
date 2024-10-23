from PageObjectModel.POMCore import POMCore

class POMClassifyCase:
  
  def ClickItem(self, instance, rowNumber):

    try:
      element = instance.window(auto_id='Main').child_window(title='Classifications').child_window(title='Bbd.Sars.CMWorkflow.ClassifyCaseWPF.Classification', found_index=0)

      element.draw_outline()

      POMCore(element).DoubleClickWithMouse()
      return True
    except:
      return False
  
  def OnCaseCreatedClickOkay(self, instance):

    try:
      element = instance.window(auto_id='Main').child_window(title="Create Case", control_type="Window").child_window(title="OK")
      
      element.draw_outline()
      element.click()

      return True
    except:
      return False