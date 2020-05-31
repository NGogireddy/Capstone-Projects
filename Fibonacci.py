# This program return's the nth Fibonacci number
# The sequence here is 0 1 1 2 3 5 8 13 21 34 57 ...
# Sample input/output:   2/1, 3/1, 5/3, 8/13

def fib(nth):
	'''
	Return the fibonacci for nth number
	'''
	first = 0
	second = 1

	index = 1

	while nth > index:
		first,second = second,first+second
		index += 1

	return first

def shell():
	'''
	Main function taking an input from user and prints the answer
	'''
	while True: 
		try: 
			number = int(input("Enter a positive number : "))
		except ValueError:
			print("It isn't a number")
			continue
		if number <= 0:
			print("Give a positive number")
			continue
		break
	print(fib(number))

if __name__ == '__main__':
	shell()
