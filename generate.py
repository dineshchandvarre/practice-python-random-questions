from random import randint
import random
def generate():
	result=""
	while True:
		words = ("anything", "something", "easy", "difficult", "answer")
		words1=("sagar","keerthi","samhith","akshara","ravi","archana","dinesh")
		x=random.choice(words)
		y=random.choice(words1)
		numbers=randint(10000,99999)
		result=x+"-"+y+"-"+str(numbers)
		yield result

for i in generate():
	print(i)
generate = generate()
print(next(generate))
print(next(generate))
print(next(generate))	