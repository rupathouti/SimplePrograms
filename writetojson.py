import json

data={}

data['people'] = []
data['people'].append({
	'name':'Thouti',
	'from':'Dussa'
})

with open('data2.txt','w') as outfile:
	json.dump(data, outfile)	
