import string
def is_pangram(sentence):
	alphabet=set(string.ascii_lowercase)
	x=""
	for letter in sentence:
		if(letter.isalpha()):
			x+=letter
	y=set(x)
	if(set(x)==set(y)):
		return True
	
