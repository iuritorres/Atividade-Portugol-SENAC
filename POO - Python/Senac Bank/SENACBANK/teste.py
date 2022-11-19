import os
import json
os.system('cls')
    
    
with open(".\SENACBANK\users.json", encoding = 'utf-8') as testeJson:
    print(testeJson.read())
    
dados = json.loads(testeJson)

print(dados)