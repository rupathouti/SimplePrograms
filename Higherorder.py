def server(v):
    print("Entering server")
    print("Task1")
    v()
    print("Task3")
    print("Leaving server")

def Client1():
    print("Entering Client1")
    server(m1)
    print("Leaving client1")

def m1():
    print("Entering m1")
    print("Task2-d")
    print("Leaving m1")

def Client2():
    print("Entering Client2")
    server(m2)
    print("Leaving client2")

def m2():
    print("Entering m2")
    print("Task2--dd")
    print("Leaving m2")

print("Welcome to Higher order function")
Client1()
Client2()
