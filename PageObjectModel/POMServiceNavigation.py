class POMServiceNavigation:
  
  def ClickWorkItem(self, instance, workItemTitle):
    
    try:
      instance.window(auto_id='Main').child_window(title=workItemTitle).click()
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
      instance.window(auto_id='Main').child_window(title='navBarTreeList').child_window(title=title).select().type_keys("{ENTER}")
      return True
    except:
      return False
    
