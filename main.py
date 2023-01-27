import random

class Card():
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def display_data(self):
		return f"{self.rank} of {self.suit}"

ranks_dict = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 11, "quenn": 12, "king": 13, "ace": 14}
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "quenn", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")
deck = []
for rank in ranks:
	for suit in suits:
		deck.append(Card(rank, suit))

game_deck = deck
random.shuffle(game_deck)
p1_deck = game_deck[0:26]
p2_deck = game_deck[26:52]
game_pile = []

game_going = True
while game_going:
	
	print(f"player 1 has a {p1_deck[0].display_data()}")
	print(f"player 2 has a {p2_deck[0].display_data()}")
	game_pile.append(p2_deck.pop(0))
	game_pile.append(p1_deck.pop(0))

	if ranks_dict[game_pile[0].rank] > ranks_dict[game_pile[1].rank]:
		print("Player one wins!\n")
		p1_deck.extend(game_pile)
		game_pile = []
	elif ranks_dict[game_pile[0].rank] < ranks_dict[game_pile[1].rank]:
		print("Player two wins!\n")
		p2_deck.extend(game_pile)
		game_pile = []

	if len(p1_deck) < 1:
		print("Player 2 wins the game!!!")
		game_going = False
	elif len(p2_deck) < 1:
		print("Player 1 wins the game!!!")
		game_going = False
