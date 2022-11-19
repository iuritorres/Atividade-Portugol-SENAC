import json

class DataManager:

    def getAllUsers():
        with open("./SENACBANK/users.json", encoding= 'utf-8', mode="r") as testeJson:
            my_data = json.loads(testeJson.read())
        
        return my_data

    def getUser(idUser):
        try:
            my_data = DataManager.getAllUsers()
            
            user = my_data["users"][str(idUser)]
            
            return user
        except KeyError:
            return "Usuario não existe"

    
    def setUser(idNewUser, Object):
        my_data = DataManager.getAllUsers()
            
        users = my_data["users"]
        users[idNewUser] = Object

        del my_data["users"]
        my_data["users"] = users
        str(my_data).replace("'", '"')
        print(my_data)

        # with open("./SENACBANK/users.json", encoding= 'utf-8', mode="w") as testeJson:
        #     testeJson.write(str(my_data))
    



BD = DataManager
BD.setUser('001', { "username": "João Vitor Souza da Silva", "password": 4341, "checkingBalance": 0, "savingsBalance": 0})