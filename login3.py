import json

path = "./users.json"

users = json.load(open(path,mode='r'))

tries = 0;

while tries < 3:
   uname = raw_input("Username: ")
   passwd = raw_input("Password: ")
   password = users.get(uname);
   if password == None:
       print("{}'s Account is not registered".format(uname))
       tries += 1
   elif password == passwd:
       print("Welcome to Concurrent Server")
       break
else:
   print("Your Tries are Exhausted")
