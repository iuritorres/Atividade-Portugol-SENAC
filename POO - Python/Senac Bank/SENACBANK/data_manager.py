# Imports
import json

# DataManager Class
class DataManager:

    # return all users of database
    def getAllUsers():
        with open("./SENACBANK/users.json", encoding= 'utf-8', mode="r") as testeJson:
            my_data = json.loads(testeJson.read())
        
        return my_data

    # return 1 user by ID
    def getUser(idUser):
        try:
            my_data = DataManager.getAllUsers()
            user = my_data["users"][str(idUser)]
            
            return user
            
        except KeyError:
            return "Usuario não existe"

    # insert new user 
    def setUser(idNewUser, Object):
        with open("./SENACBANK/users.json", encoding='utf-8', mode="r+") as jsonFile:

            # recieve new user data
            teste = f'{idNewUser}: {Object}'

            fileData = json.load(jsonFile)              # load file in fileData
            fileData['users'][idNewUser] = Object       # set new user in fileData
            jsonFile.seek(0)                            # set handle position at 0
            json.dump(fileData, jsonFile, indent=4)     # dumps back the new dataBase to jsonFile

