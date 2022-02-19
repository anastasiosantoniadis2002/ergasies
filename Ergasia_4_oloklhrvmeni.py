import random
FYLLO=[i for i in range(1,11)]
XRWMA=["C","S","H","D"]
FIGOURES=["J","Q","K"]
FYLLO=FYLLO+FIGOURES

def get_card_value(c):
	if c[1] in FIGOURES:
		return 10
	else:
		return c[1]

def sum_cards(LST):
	score = 0
	for c in LST:
		score += get_card_value(c)
	return score
paixtis1 = 0
paixtis2 = 0
isopalia = 0
for i in range(100):
	DECK=[]
	for i in XRWMA:
		for j in FYLLO:
			DECK.append([i,j])
	random.shuffle(DECK)
	
	# moirase xartia
	comp_cards = [DECK[0],DECK[1],DECK[2]]
	my_cards = [DECK[3],DECK[4]]

	comp_score=sum_cards(comp_cards)
	print(comp_cards,comp_score)
	my_score=sum_cards(my_cards)
	print(my_cards,my_score)

	if my_score>comp_score:
		print("kerdises!")
		paixtis2 += 1
	elif comp_score>my_score:
		print("exases :(")
		paixtis1 += 1
	else:
		print("pame pali...")
		isopalia += 1
print("o protos paixtis kerdise " , paixtis2 , "fores")
print("o deuteros paixthw kerdise" , paixtis1 , "fores")
print("upirje isopalia " , isopalia , "fores")
paixtisx2 = 0
paixtisx1 = 0
isopaliax = 0
for i in range(100):
	DECK = []
	for i in XRWMA:
		for j in FYLLO:
			DECK.append([i, j])
	random.shuffle(DECK)
	while get_card_value(DECK[0])!= 10:
		random.shuffle(DECK)
	# moirase xartia
	comp_cards = [DECK[0], DECK[1], DECK[2]]
	h = 3
	while get_card_value(DECK[h]) == 10:
		if h == 3:
			h = h + 2
		else:
			h += 1
	my_cards = [DECK[h], DECK[4]]

	comp_score = sum_cards(comp_cards)
	print(comp_cards, comp_score)
	my_score = sum_cards(my_cards)
	print(my_cards, my_score)

	if my_score > comp_score:
		print("kerdises!")
		paixtisx2 += 1
	elif comp_score > my_score:
		print("exases :(")
		paixtisx1 += 1
	else:
		print("pame pali...")
		isopaliax += 1
print("o protos paixtis kerdise ", paixtisx2, "fores")
print("o deuteros paixthw kerdise", paixtisx1, "fores")
print("upirje isopalia ", isopaliax, "fores")
