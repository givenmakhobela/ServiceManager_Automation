import allure
import datetime

def AllureStep(message):
  allure.attach(message, name="Step Result:", attachment_type=allure.attachment_type.TEXT)

def AllureScreenshot(context):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S_%f")
    name = f"ServiceManager_{now}.png"
    try:
        screenshot = context.top_window().capture_as_image()
        screenshot.save(f'Images\{name}')

        allure.attach.file(
            f'Images\{name}', name=f"Screenshot: {name}", attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        allure.attach(
            str(e), name="Screenshot Error", attachment_type=allure.attachment_type.TEXT
        )