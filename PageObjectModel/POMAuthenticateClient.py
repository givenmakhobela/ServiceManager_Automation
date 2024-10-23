
class POMAuthenticateClient:

  def SearchButton(instance):

    try:
      element = instance.window(auto_id='Main').child_window(title="Search", control_type="Button")
      element.draw_outline()
      element.click()

      return True
    except:
      return False