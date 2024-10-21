import pytest
from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
from helper.ServiceManagerOperator import ServiceManagerOperator


@pytest.fixture
def context():
  serviceManagerOperator = ServiceManagerOperator()

  return serviceManagerOperator.StartServiceManager()

