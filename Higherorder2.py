def server(v,y):
    print("Entering server")
    print("Task1")
    x=3
    v(x,y)
    print("Task3")
    print("Leaving server")

def Client1():
    print("Entering Client1")
    server(m1,33)
    print("Leaving client1")

def m1(p,q):
    print("Entering m1")
    print("Task2-d")
    print(p+q)
    print("Leaving m1")

def Client2():
    print("Entering Client2")
    server(m2,99)
    print("Leaving client2")

def m2(p,q):
    print("Entering m2")
    print("Task2--dd")
    print(p-q)
    print("Leaving m2")

print("Welcome to Higher order function")
Client1()
Client2()
