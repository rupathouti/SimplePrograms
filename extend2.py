print("Entering Python Program")

#Creating a List
a = [10,20,30,40]

print("List values before Extending",a)

a.extend([50,60])
print("List values after Extending via List literal",a)

b = [70,80]
print("Values in list b")

a.extend(b)
print("List values after Extending via list b",a)
print("List b is not affected by this extention",b)

print("Leaving Python Program")
