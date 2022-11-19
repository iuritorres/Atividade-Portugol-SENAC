import os
import json

os.system('cls')

file = open('SENACBANK\users.json', )

users = json.load(file)

for user in users:
    print(user)

file.close()