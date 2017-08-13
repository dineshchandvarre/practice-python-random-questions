
def dic(dog_owned_by):
	dog_owned_by = {'Peter': 'Furry', 'Sally': 'Fluffy'}
	dogs = []
	for owner in dog_owned_by:
		dogs.append(owner)
	return dogs
print(dic({'Peter': 'Furry', 'Sally': 'Fluffy'}))