def recurring(arr):
	dictionary={}
	s=0
	for i in arr:
		dictionary[i]=arr.count(i)
	s=max(dictionary)
	return s
	# li=[i for i in arr if arr.count(i)<=len(arr)]

	# return sorted(li)[::-1]
print(recurring([1,3,2,3,4,5,4,4,3,2,2,2,1,9,9,9,9,9,9,9,9]))