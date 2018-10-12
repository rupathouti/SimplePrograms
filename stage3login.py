users = {}
file = open("./list.txt",mode='r')
for data in file.readlines():
    l=data.strip().split(",")
    users[l[0]] = l[1]

tries = 0

while tries < 3:
   uname = input("Username: ")
   passwd = input("Password: ")
   rpass = users.get(uname)
   if rpass == None:
       print("You are not a registered user")
       tries += 1
   elif passwd == rpass:
       print("Welcome {} you are logged in!".format(uname))
       break
   else:
       print("You entered the worng password")
       tries += 1
else:
   print("Your Tries are Exhausted")
