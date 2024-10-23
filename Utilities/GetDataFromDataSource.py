import csv

class GetDataFromDataSource():

  def GetUnRegisteredUsers():
    with open('Data/UnregisteredTaxNoUsers.csv', mode ='r')as file:
      csvFile = csv.reader(file)
      for lines in csvFile:
            return lines
