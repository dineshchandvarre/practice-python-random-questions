def math_op(arr):
	result=[]
	for i in array:
		result.append(operation(i))
	return result
def operation(x):
	x=x.split("+")
	ab=map(int,x[0].split("/"))
	cd=map(int,x[1].split("/"))
	return test(ab[0],ab[1],cd[0],cd[1])
def test(a,b,c,d):
	return ((a*d)+(b*c))/(b*d)
array=["22/34+35/67","2/3+35/6","67/34+31/69","1/2+1/3"]

print(math_op(array))
