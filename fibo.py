# def fibo(n):
# 	li=[]
# 	i=0
# 	for i in range(n):
# 		if(i==0 or i==1):
# 			x=1
# 		else:
# 			x=li[i-1]+li[i-2]
# 		li.append(x)
# 	return li
# print(fibo(20))

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib, range(1, 10000))