'''
Solution for FizzBuzz problem
'''

def main(): 
	'''
	Prints numbers from 1 to 100 
	if multiple of 3 it is a Fizz
	if multiple of 5 it is a Buzz
	if multiple of 3 and 5 it is a FizzBuzz
	'''

	for num in range(1,101): 
		if num%3 == 0 and num%5 == 0: 
			print('FizzBuzz')
		elif num%3 == 0: 
			print('Fizz')
		elif num%5 == 0:
			print('Buzz')
		else:
			print(num)

if __name__ == '__main__':
	main()