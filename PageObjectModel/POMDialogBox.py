from PageObjectModel.POMCore import POMCore

class POMDialogBox:
  
  def OnCaseCreated(self, instance, rowNumber):

    try:
      element = instance.window(auto_id='Main').child_window(title='Classifications').child_window(title='Bbd.Sars.CMWorkflow.ClassifyCaseWPF.Classification', found_index=0)

      POMCore(element).doubleClickWithMouse()
      return True
    except:
      return False