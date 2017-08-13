def di(dictionary):
	empty={}
	for i in dictionary:
		
		if (i=='2' in dictionary):
			dictionary['2']='sagar'
	return dictionary
		
	
		
	
print(di({'1':'king','2':'queen'}))
