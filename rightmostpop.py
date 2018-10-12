print("Entering Python Program")

#Creating a List
a = [10,20,30,40]

print("List values before insertion",a)

a.insert(1,333)

print("List values after insertion at index 1",a)

a.pop(1)

print("List value after value at index 1 is popped",a)

r = a.pop()

print("The popped value is ",r)

print("List after popping rightmost value is ",a)

print("Leaving Python Program")
