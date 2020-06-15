'''
This module will print the number names upto 1 billion. It is easily expandable for any numbers. 
To expand it make changes in get_name module
'''

NAMES_1 = ['Zero ','One ','Two ','Three ','Four ','Five ','Six ','Seven ','Eight ','Nine ','Ten ',
'Eleven ','Twelve ','Thirteen ','Fourteen ','Fifteen ','Sixteen ','Seventeen ','Eighteen ','Nineteen ']
NAMES_2 = ['','Ten ','Twenty ','Thirty ','Fourty ','Fifty ','Sixty ','Seventy ','Eighty ','Ninety ']

def get_last_two_name(number): 
	'''
	Returns the number name of last two digits
	'''

	if 0 < number <= 19:
		return NAMES_1[number]
	elif number%10 == 0: 
		return NAMES_2[int(number/10)]
	else: 
		return NAMES_2[int(number/10)] + NAMES_1[int(number%10)]
	return ''

def get_last_three_name(number): 
	'''
	Returns the number name of the last three digits
	'''

	if int(number/100) == 0: 
		return get_last_two_name(int(number%100))
	else:
		last_two = get_last_two_name(int(number%100))
		if last_two == '':
			return NAMES_1[int(number/100)] + 'Hundred '
		else:
			return NAMES_1[int(number/100)] + 'Hundred and ' +  last_two

def get_name(number): 
	'''
	Main logic to prepare the names
	'''

	part1 = ''
	part2 = ''
	part3 = ''

	if number == 0: 
		return 'Zero '

	if int(number/1000000) > 0:
		part3 = get_last_three_name(int(number/1000000)) + 'Million '
	number %= 1000000

	if int(number/1000) > 0: 
		part2 = get_last_three_name(int(number/1000)) + 'Thousand '
	number %= 1000

	part1 = get_last_three_name(number)

	return part3+part2+part1

def main():
	'''
	Main logic to ask the number and print the name
	'''

	while True: 
		try: 
			number = int(input('Enter a number below 1 billion to see its name : '))
		except ValueError: 
			print('Enter only digits without any special characters including commas (,). Try again')
		else: 
			if 0 <= number < 1000000000: 
				print(f'The number name for {number} is {get_name(number)}')
				break
			else:
				print('Enter a number without +/- sign and less than one billion. Try again')
			
if __name__ == '__main__':
	main()
