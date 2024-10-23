import allure

def AllureStep(message):
  allure.attach(message, name="Step Result:", attachment_type=allure.attachment_type.TEXT)