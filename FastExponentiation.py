'''
This program returns the fast exponentiation of a**b in the O(log n)
'''

def exp_answer(base,power): 
	'''
	returns base**power in O(log n)
	'''
	if base<2: 
		return base
	if power<2: 
		return base
	else: 
		if power%2 == 0: 
			return exp_answer(base,power/2)**2
		else: 
			return base * exp_answer(base,int((power-1)/2))**2

def main(): 
	'''
	get the base and power from the user and call the function
	'''
	while True: 
		try: 
			base = int(input('Give the base (an integer) :'))
		except ValueError: 
			print('Value error, enter an integer. Try again')
		else: 
			if base>=0:
				break 

	while True: 
		try: 
			power = int(input('Give the power (an integer) :'))
		except ValueError: 
			print('Value error, enter an integer. Try again')
		else:
			if  power>0:
				break 

	answer = exp_answer(base,power)

	print(f'{base} raised to the power of {power} is {answer}')

if __name__ == '__main__':
	main()