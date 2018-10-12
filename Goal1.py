print("Welcome to GOAL Improvement tool\n")

print("May I know your Name?\n")
Name=raw_input()

print "Do you have a goal",Name
Goal=raw_input().lower()

if(Goal=="yes"):
	print("Tell me your Goal in single word?")
	Goal1=raw_input()
else:
	exit()

print("How often you are practicing?")
print("Daily/Weekly")
practice=raw_input().lower()

if(practice=="daily") and (practice!=""):
	print("How many hours daily?")
	hours=raw_input()
	if(hours>=5):
		print("Good!!! Soon you will achieve your GOAL.")
	else:
		print("Need more practice") 
else:
	print("How many hours weekly?")
	hours=raw_input()
	if(hours>=20):
		print("Good!!! Soon you will achieve your GOAL.")
	else:
		print("Need more practice") 
