# NextPrimeNumber.py This is solution for finding the prime number until user wants them.

from math import isqrt

PRIMES_LIST = [2,3]

def is_prime(number):
	'''
	this function checks if the number is prime and returns it.
	It stores the prime numbers in a list. They will help us for finding next prine. 
	'''

	square_root = isqrt(number)

	for num in PRIMES_LIST:
		if number%num == 0: 
			return(False)
		elif num > square_root:
			PRIMES_LIST.append(number)
			return(True)

def next_prime():
	'''
	This function will return the next prime number
	'''

	number = PRIMES_LIST[-1] + 2

	while True:
		if is_prime(number):
			break
		number += 2
	
def main():
	'''
	Give a prime number and ask user to continue Y/N
	'''
	cont = 'y'

	while cont == 'y': 
		try: 
			print(f'{PRIMES_LIST[-2]} is a prime.')
			cont = input(' Want to see next (Y/N) ? ').lower()
		except:
			print('Something went wrong. Enter Y to see next prime or N to stop')
			continue

		if cont not in 'yn':
			print('Enter Y to see next prime or N to stop')
			continue
		
		if cont == 'y':
			next_prime()

if __name__ == '__main__':
	main()
