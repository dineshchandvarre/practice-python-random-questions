def li(arr,num):
	
	for i in range(len(arr)-num):
		s=arr[i:i+num]
		strin=""
		for y in s:
			strin+=str(y)
		yield strin


for x in li([1,2,4,5,9,3,2,6,7,2,6],3):
	print (x)


