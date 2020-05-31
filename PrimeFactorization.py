# PrimeFactorization.py This is solution for finding all the prime factors of a number if present.

def find_prime_factors(number):
	'''
	this function prepares the list of prime factors and returns it
	'''

	pf_list = [1]

	if number%2 == 0 :
		pf_list.append(2)
		while number%2 == 0:
			number /= 2
	
	index = 3

	while index <= number:
		if number%index == 0: 
			pf_list.append(index)
			while number%index == 0:
				number /= index
	
		index += 2
	
	return pf_list

def main():
	'''
	Gets the user input and calls the find factorial function
	'''

	while True: 
		try: 
			number = int(input('Enter a number to see its prime factors : '))
		except ValueError:
			print('Enter a positive number. Try again')
			continue
		if number < 1:
			print('Enter a positive number. Try again')
			continue
		break

	prime_factors = find_prime_factors(number)

	print(prime_factors)

if __name__ == '__main__':
	main()
