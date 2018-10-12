myfile=open("test.txt","r")

for data in myfile.readlines():
	print("test.txt contains->", data)
