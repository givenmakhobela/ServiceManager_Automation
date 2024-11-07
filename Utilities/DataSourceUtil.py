import csv

class DataSourceUtil():

  def GetUnregisteredUser(self):
    with open('Data/UnregisteredSARSUsers.csv', mode ='r')as file:
      csvFile = csv.reader(file)
      for lines in csvFile:
        return lines
  
  def GetRegisteredUser(self):
    with open('Data/RegisteredSARSUsers.csv', mode ='r')as file:
      csvFile = csv.reader(file)
      for lines in csvFile:
        return lines
  
  def GetEntityRegistrationXML(self):
    with open('Data/EntityRegistration.xml.txt', 'r') as file:
      return file.read()
  
  def AddUnregisteredUserToRegisteredUsersFile(self):
    initalCounter = 0
    registeredUser = None
    unRegisteredUsers = []
     
    with open('Data/UnregisteredSARSUsers.csv', mode ='r')as file:
      csvFile = csv.reader(file)

      for line in csvFile:
        if initalCounter == 0:
          registeredUser = line
          initalCounter = 1
        else:
          unRegisteredUsers.append(line)
    
    self.AddUserAsSARSRegisteredUser(registeredUser)
    self.ReturnUnregisteredUsers(unRegisteredUsers)
  
  def AddUserAsSARSRegisteredUser(self, user):
    with open('Data/RegisteredSARSUsers.csv', 'a', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(user)
  
  def ReturnUnregisteredUsers(self, users):
    with open('Data/UnregisteredSARSUsers.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerows(users)
