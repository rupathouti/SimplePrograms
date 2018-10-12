users={
"name":"RupaThouti",
"goal":"Skipping",
"opportunities":"Gym"
	}

def daily():
	
	print("How many hours daily?")
	hours=int(raw_input())
	
	if(hours>=5):
		print("Good!!! Soon you will achieve your GOAL.")
	
	else:
		print("Need more practice") 
	
def weekly():
	print("How many hours weekly?")
	hours=int(raw_input())

	if(hours>=20):
		print("Good!!! Soon you will achieve your GOAL.")
	else:
		print("Need more practice") 
	

print("Welcome to RRR(Repetition,Reflection,Result) tool\n")


print(users["name"])


print "Do you have a goal",name
Goal=raw_input().lower()

if(Goal=="yes"):
	print("Tell me your Goal in single word?")
	print(users["goal"])
else:
	exit()

print("How many opportunities do you have to achieve your goal?")
oppor=int(raw_input().lower())

print("What are they, please specify with comma separation...")
print(users["opportunities"])


print("How often you are practicing?")
print("Daily/Weekly")
practice=raw_input().lower()
if(practice=="daily"): 
	daily()
else:
	weekly()

