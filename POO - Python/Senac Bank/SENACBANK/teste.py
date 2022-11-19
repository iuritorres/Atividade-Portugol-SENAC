import os
import json
os.system('cls')
    
    
with open("./SENACBANK/users.json", encoding= 'utf-8', mode="r") as testeJson:
    my_data = json.loads(testeJson.read())
    

print(my_data)
print(type(my_data))