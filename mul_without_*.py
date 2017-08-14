"""Implement multiplication without using the multiplication operator"""
def mul(x,y):
	result=0
	for i in range(y):
		result+=x
	return result
print(mul(2,5))