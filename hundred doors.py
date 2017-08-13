def hundred_doors(x,y):
	doors=["c" for i in range(1,101)]
	for i in range(1,y+1):
		for j in range(len(doors)):
			if j%i==0:
				if doors[j]=="o":
					doors[j]="c"
				elif doors[j]=="c":
					doors[j]="o"
	return doors[x]

print(hundred_doors(4,4))