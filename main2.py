import random

deck = list(range(2, 15)) * 4
random.shuffle(deck)
p1_deck = deck[:26]
p2_deck = deck[26:]
game_pile = []

while len(p1_deck) > 0 and len(p2_deck) > 0:
	
	p1Card = p1_deck.pop()
	p2Card = p2_deck.pop()
 
	game_pile.append(p1Card)
	game_pile.append(p2Card)
	print(f"Player 1 has a {p1Card}\n Player 2 has a {p2Card}")

	if p1Card > p2Card:
		print("Player 1 wins!")
		p1_deck.extend(game_pile)
		game_pile = [] 

	elif p1Card < p2Card:
		print("Player 2 wins!")
		p2_deck.extend(game_pile)
		game_pile = []

	elif p1Card == p2Card: 
		print("War!")

if len(p2_deck) > len(p1_deck):
	print("Player two wins the game!!!")
else: 
	print("Player one wins the game!!!")
