"""
23March2019
A simulation to run the game Blackjack

Notes on the rules of the games
- Player options: hit or stay (not double down, split, surrender)
- Dealer will draw on a soft 17.
- Bets pay out 1:1, Blackjack pays out 3:2.
"""

import os
import random


def blackjack():
	winnings = money
	deck = [
		'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
		'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
		'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
		'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
	]

	dealer_hand = []
	player_hand = []

	def hand_total(hand):
		"""A function that calculates the card total and returns the sum. """

		total = 0
		non_aces = [card for card in hand if card != 'A']
		aces = [card for card in hand if card == 'A']

		for card in non_aces:
			if card in 'JQK':
				total += 10
			else:
				total += int(card)
		for card in aces:
			# this avoids a double ace bust.
			if len(aces) == 2 and total <= 9:
				total += 11
			if len(aces) < 2 and total <= 10:
				total += 11
			else:
				total += 1
		return total

	def show_hands():
		print("Dealer's hand: [{}] (Dealer's Total: {})".format(']['.join(dealer_hand),	hand_total(dealer_hand)))
		print("Player's hand: [{}] (Player's Total: {})".format(']['.join(player_hand), hand_total(player_hand)))

	random.shuffle(deck)
	for i in range(2):
		player_hand.append(deck.pop())
		dealer_hand.append(deck.pop())

	while True:
		"""Script to manage a hand."""
		os.system('cls' if os.name == 'nt' else 'clear') # Tidies up.

		print('\ndealer hand: [{}][?]'.format(dealer_hand[0]))
		print('player hand: [{}] (Player Total: {})'.format(']['.join(player_hand), hand_total(player_hand)))

		if len(player_hand) == 2 and hand_total(player_hand) == 21:
			if hand_total(player_hand) != hand_total(dealer_hand):
				# player wins 3:2 times the amount of the bet. Another popular option is 6:5.
				winnings_increase = int(int((3 * int(bet) / 2)))
				print(f"Blackjack, Player wins ${winnings_increase}")
				winnings += int(winnings_increase)
				print(f"current money: ${winnings}")
				break
			else:
				# on a push neither player nor dealer wins.
				print('Push, no one wins.')
				print(f"current money: ${winnings}")
				break

		print('What would you like to do?')
		player_choice = input('Hit or stay? [H/S]')

		if player_choice.lower() == 'h':
			# draw a new card and end if player busted.
			player_hand.append(deck.pop())
			hand_total(player_hand)
			if hand_total(player_hand) > 21:
				show_hands()
				print(f"Player busted, and loses ${bet}")
				winnings -= int(bet)
				print(f"Current money: ${winnings}")
				break

		if player_choice.lower() == 's':
			# resolve dealer's hand and determine the winner.
			while hand_total(dealer_hand) < 17:
				# dealer will draw until they are at or above 17.
				dealer_hand.append(deck.pop())
			if hand_total(dealer_hand) == 17 and 'A' in dealer_hand:
				# Dealer will draw on a soft 17
				dealer_hand.append(deck.pop())
			show_hands()
			if hand_total(dealer_hand) > 21:
				print(f"Dealer busted. You win ${bet}!")
				winnings += int(bet)
				print(f"Current money: ${winnings}")
				break
			if hand_total(player_hand) > hand_total(dealer_hand):
				print(f'You win ${bet}!')
				winnings += int(bet)
				print(f"Current money: ${winnings}")
				break
			if hand_total(player_hand) < hand_total(dealer_hand):
				print(f'Dealer wins, you lose ${bet}.')
				winnings -= int(bet)
				print(f"Current money: ${winnings}")
				break
			if hand_total(player_hand) == hand_total(dealer_hand):
				print('Push, no one wins.')
				winnings += int(bet)
				print(f"Current money: ${winnings}")
				break
			break

		if player_choice.lower() == 'q':
			# stops the program.
			print(f"You leave with ${winnings} winnings.")
			break
	with open('winnings.txt', 'w') as w:
		w.write(str(winnings))
	w.close()


active = True
while active:
	with open('winnings.txt', 'r') as f:
		contents = f.read()
	money = (int(contents))
	f.close()
	print(f"\nCurrent money: ${money}")
	choice = input("Would you like to play a hand of Blackjack? (Y/N)")
	if choice.lower() == 'y':
		bet = input("How much would you like to bet?")
		blackjack()
	elif choice.lower() == 'n':
		print("Thank you and goodbye!")
		active = False
	elif choice.lower() != 'y' or 'n':
		print("You must choose 'Y' for yes or 'N' for no.")
