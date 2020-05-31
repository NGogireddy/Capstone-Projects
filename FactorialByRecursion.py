# This is the solution for finding the factorial of a number using recursion

def factorial(number=0):
	'''
	This function returns the factorial of positive numbers
	'''

	if number <= 1:
		return 1
	else:
		return number*factorial(number-1)


def shell(): 
	'''
	This is the main function to take user input and pring the factorial
	'''

	while True:
		try:
			number = int(input('Enter a positive number :'))
		except ValueError:
			print("It isn't a number. Try again")
			continue
		if number < 0: 
			print('Need a positive number. Try again')
			continue
		break

	print(f'Factorial of {number} is {factorial(number)}')

if __name__ == '__main__':
	shell()
