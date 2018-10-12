names = ['amit','parag','mangesh']
domains = ['google.com','yahoo.com','rajeshpatkar.com']
print("Please Enter email id")
email = raw_input()
emailparts = email.split("@");
if(emailparts[0] in names and emailparts[1] in domains) :
    print("Valid Email ID")
else:
    print("Invalid Email ID")
