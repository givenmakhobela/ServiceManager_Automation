from helper.ServiceManagerOperator import ServiceManagerOperator

def before_all(context):
  context = ServiceManagerOperator().StartServiceManager()
  yield context

