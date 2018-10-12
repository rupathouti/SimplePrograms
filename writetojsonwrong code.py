import json

def writeToJSONFile(path,filename,data):
	filePathNameWExt='./'+path+'/'+'fileName'+'.json'
	print("filePathNameWExt")
	with open(filePathNameWExt,'w')as fp:
		json.dump(data,fp)


path = "./"
fileName='rupa.json'


data={}

data['Rupa'] ='Venu'
data['Bhaskar'] ='Poshaiah'

writeToJSONFile(path,filename,data)
