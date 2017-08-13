""" Find first two integers in a large array where the sum of integers will be 100 or x"""
import random
def large_array(x):
	array=[]
	a=0
	for i in range(100):
		r= random.randrange(10)
		array.append(r)
	for j in range(len(array)):
		if array[j]<10:
			y=abs(10-array[j])
			if y in array[:j]:
				a=array[:j].index(y)

	return (y,array[j]),(a,j)
print(large_array(100))

