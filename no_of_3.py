def no_of_3(x):
	result=0
	for i in range(1,x+1):
		y=str(i)
		result+=y.count("1")
		print(y,y.count("0"))
	return result
print(no_of_3(1000))
