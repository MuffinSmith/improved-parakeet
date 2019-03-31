# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
def getCreds():
    userInfo = {}
    userInfo["username"] = input("Enter user name: ")
    userInfo["password"] = input("Enter password: ")
    return userInfo

def checkLogin(userInfo, adminList):
    for x in adminList:
        if(x["username"] == userInfo["username"]):
            if(x["password"] == userInfo["password"]):
                print("YOU HAVE LOGGED IN!")
                return False
    return True        

while  checkLogin(getCreds(),adminList):
    print("----------")

