
#Overwrite the existing one and write the list content
myfile=open("test1.txt","w")
list=[10,20,30,40,50,60,70,80]
for data in list:
	print("Writing->",data)
	myfile.write("{}\n".format(data))
myfile.close()
