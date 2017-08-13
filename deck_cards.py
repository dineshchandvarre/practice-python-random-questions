import random
def deck_cards():
	deck_of_cards=[]
	colours=["Spade","Hearts","Diamond","Club"]
	series=map(str,[2,3,4,5,6,7,8,9,10,"J","Q","K","A"])
	for x in colours:
		for y in series:
			deck_of_cards.append(x+" "+y)
	return random.choice(deck_of_cards),len(deck_of_cards)

print(deck_cards())