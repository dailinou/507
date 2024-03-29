import random
import unittest

# SI 507 Fall 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time:
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list


	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p1 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card) 

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))

	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########
#






##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):


	# this is a "test"
	def test_create(self):
		card = Card()
		self.assertEqual(card.suit, "Diamonds")
		self.assertEqual(card.rank, 2)



	#TEST 1
	def test_rank12_equals_queen(self):
		card =  Card(rank=12)

		self.assertEqual(card.rank, "Queen")



	#TEST 2
	def test_suit1_equals_clubs(self):
		card = Card(suit = 1)

		self.assertEqual(card.suit,"Clubs")



	#TEST 3
	def test_suit3rank13_equals_kingofspades(self):
		card = str(Card(suit = 3, rank = 13))

		self.assertEqual(card,"King of Spades")



	#TEST 4
	def test_deck_has_52cards(self):
		deck = Deck()

		self.assertEqual(len(deck.cards),52)



	#TEST 5
	def test_pop_card_return_a_card(self):
		deck = Deck() #how to return all card instances?
		pop_card = deck.pop_card()

		self.assertIsInstance(pop_card, Card)



	#TEST 6
	def test_pop_card_reduce_card(self):
		deck1 = Deck()
		deck2 = Deck()
		deck1.pop_card()

		self.assertEqual(len(deck1.cards),len(deck2.cards)-1)



	#TEST 7
	def test_replace_card_one_more_card(self):
		deck = Deck()
		pop_card1 = deck.pop_card()
		pop_card2 = deck.pop_card()
		self.assertEqual(len(deck.cards),50)

		deck.replace_card(pop_card1)
		self.assertEqual(len(deck.cards),51)



	#TEST 8
	def test_replace_same_card(self):
		deck = Deck()
		pop_card1 = deck.pop_card()
		pop_card2 = deck.pop_card()

		deck.replace_card(pop_card1)
		self.assertEqual(len(deck.cards),51)

		deck.replace_card(pop_card1)
		self.assertEqual(len(deck.cards),51)



	#TEST 9
	def test_play_game(self):
		game_return = play_war_game()

		self.assertIsInstance(game_return, tuple)
		self.assertEqual(len(game_return),3)


		game_return_1 = game_return[0]

		self.assertIsInstance(game_return_1, str)



	#TEST 10
	#Test that if you revoke the shuffle method, the deck is not in the same order anymore.

	def test_shuffle(self):
		deck1 = Deck()
		deck1.shuffle()
		deck2 = Deck()

		self.assertNotEqual(deck1,deck2)








#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
