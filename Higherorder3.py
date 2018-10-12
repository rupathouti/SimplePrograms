def server(v,y):
    print("Entering server")
    print("Task1")
    x=3
    v(x,y)
    print("Task3")
    print("Leaving server")

g=9
def Client1():
    print("Entering Client1")
    s=7
    # Captured variable
    def m1(p,q):
        print("Entering m1")
        global g
        nonlocal s
        k=p+q+s
        s=p*3+q+g
        print(s)
        print(k)
        print("Leaving m1")
    server(m1,99)
    print("Leaving Client1")
Client1()
Client1()
