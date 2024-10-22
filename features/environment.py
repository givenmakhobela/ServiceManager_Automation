from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
from helper.ServiceManagerOperator import ServiceManagerOperator

def before_all(context):
  context = ServiceManagerOperator().StartServiceManager()
  yield context

