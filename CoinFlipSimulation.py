# CoinFlipSimulation.py This is solution for coin flip problem

import random

def flip_the_coin():
	'''
	this function returns a random value Heads/Tails
	'''

	return random.choice(['Heads','Tails'])

def main():
	'''
	Gets the user input and flips the coin so many times while tracking the outcome
	'''

	while True: 
		try: 
			times = int(input('How many times do you want to flip : '))
		except ValueError:
			print('Enter a positive number. Try again')
			continue
		if times < 1:
			print('Enter a positive number. Try again')
			continue
		break

	heads_count = 0
	tails_count = 0

	for index in range(times):

		if flip_the_coin() == 'Heads': 
			heads_count += 1
		else:
			tails_count += 1

	print(f'We have flipped the coin {times} times.')
	print(f'Heads count: {heads_count}')
	print(f'Tails count: {tails_count}')

if __name__ == '__main__':
	main()
