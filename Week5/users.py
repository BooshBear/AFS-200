
from doctest import testfile
import json
from urllib import response
import requests

class User():
    def __init__(self, First_Name, Last_Name, Email_Address, Username, Password, UUID, Phone, Cell, Picture_Large, Picture_Thumbnail):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Email_Address = Email_Address
        self.Username = Username
        self.Password = Password
        self.UUID = UUID
        self.Phone = Phone
        self.Cell = Cell
        self.Picture_Large = Picture_Large
        self.Picture_Thumbnail = Picture_Thumbnail

    def __str__(self):
            retStr = self.First_Name + " "
            retStr += self.Last_Name 
            retStr += "("+ self.Email_Address + ")"
            return retStr
    

class AuthorizedUsers():
    def __init__(self):
        self.Users = []

    def addUser(self, user):
        self.Users.append(user)

    def showUser(self):
        for user in self.Users:
            print(user)

    
def getData():
    URL = "https://randomuser.me/api/?nat=US&results=10"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status
        response_JSON = response.json()
        return response_JSON["results"]

    except requests.exceptions.HTTPError as errh:
        print(errh)

theUsers = AuthorizedUsers()
jsonUserData = getData()

for x in jsonUserData:
    fname = x["name"]["first"]
    lname = x["name"]["last"]
    eml = x["email"]
    username = x["login"]["username"]
    password = x["login"]["password"]
    uuid = x["login"]["uuid"]
    phone = x["phone"]
    cell = x["cell"]
    lpic = x["picture"]["large"]
    tpic = x["picture"]["thumbnail"]

    test = User(fname,lname,eml,username,password,uuid,phone,cell,lpic,tpic)
    theUsers.addUser(test)

theUsers.showUser()