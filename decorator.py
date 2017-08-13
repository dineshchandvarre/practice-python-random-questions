import time
def decorator(xyz):
	def wrap():
		t1=time.time()
		xyz()
		t2=time.time()
		print("xyz took "+ str(t2-t1)+" time to run")
	return wrap
@decorator
def index(i):
	i=[2,4,7,9,34,21]
	print(max(li))
index()