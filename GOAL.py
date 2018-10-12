cycles= 0
hours=0

def repetition(amount):
    global cycles
    global hours
    if(cycles > 0):
        balance = balance + amount
        lt = amount

def reflecion(amount):
    global balance
    global lt
    if(balance >= amount):
        balance = balance - amount
        lt = -amount

def feedback():
    print("|Statment|")
    print("Balance =",balance)
    print("Last Transaction =",lt)
   

print("Welcome to GOAL Improvement tool\n")
print("Help-")
print("Type rep to Repetition")
print("Type ref to Reflection")
print("Type FB to print the Feedback")
print("Type h to access Help")
print("Type q to Quit\n")

print("May I know your Name?\n")
Name=raw_input()

print "Do you have a goal",Name
Goal=raw_input()
if(Goal=="yes"):
	print("Tell me your Goal")
	Goal1=raw_input()
else:
	exit()
