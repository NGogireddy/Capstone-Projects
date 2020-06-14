'''
This prints first 8 happy numbers
'''

HAPPY_NUMBERS = set()
UNHAPPY_NUMBERS = set()

def get_digits(number):
	'''
	returns the digits in the number
	'''
	numbers = []

	while number>0:
		numbers.append(number%10)
		number = int(number/10)
	return numbers

def check_for_happy(number): 
	'''
	Checks if the number is happy and returns true or false. 
	It also adds the other happy numbers found in the process 
	'''
	global HAPPY_NUMBERS
	global UNHAPPY_NUMBERS
	checklist = set()
	if number in HAPPY_NUMBERS: 
		return True
	elif number in UNHAPPY_NUMBERS:
		return False
	else: 
		while True: 
			squares_sum = sum(list(map(lambda x: x**2,get_digits(number))))
			checklist.add(number)
			if squares_sum == 1: 
				HAPPY_NUMBERS = HAPPY_NUMBERS.union(checklist)
				return True
			else:
				if squares_sum in checklist:
					UNHAPPY_NUMBERS = UNHAPPY_NUMBERS.union(checklist)
					return False
				number = squares_sum

def main(): 
	'''
	Main logic to get first 8 happy numbers
	'''
	count = 0
	number = 1
	while count<8:
		if check_for_happy(number): 
			if len(HAPPY_NUMBERS) >= 8:
				happy_list = list(HAPPY_NUMBERS)
				happy_list.sort()
				if number ==  happy_list[7]:
					print('First 8 happy numbers are :')
					for num in happy_list[0:8]: 
						print(num)
			count += 1
		number+= 1

if __name__ == '__main__':
	main()