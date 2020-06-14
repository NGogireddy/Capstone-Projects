# This program converts a number to binary and vice versa

def bin_to_dec(str_binary): 
	'''
	This will take a binary input as string and gives the decimal value of it.
	Validations to the input should be carried prior to this call. 
	'''

	decimal = 0
	rev_binary = str_binary[-1::-1]

	for index,digit in enumerate(rev_binary): 
		decimal += int(digit) * 2**int(index)

	return decimal

def dec_to_bin(int_number): 
	'''
	This will take a number as interger and gives the binary representation of it. 
	Validations to the input should be carried prior to this call. 
	'''

	output = ''
	remainder_list = []

	while True: 
		if int_number <= 1: 
			remainder_list.append(str(int_number))
			break
		remainder_list.append(str(int_number%2))
		int_number = int_number//2

	output = ''.join(remainder_list)[-1::-1]
	return output

def get_binary(): 
	'''
	This will ask user for a binary number
	'''

	bad_input = True

	while bad_input:
		bin_number = input("Enter a binary number (1's and 0's) : ")
		bad_input = False
		for a in bin_number: 
			if a not in '01': 
				print('Enter number without any characters/spaces or other digits')
				bad_input = True
				break
		if not bad_input:
			return bin_number

def get_decimal():
	'''
	This will ask user for a decimal number
	'''

	while True:
		try: 
			dec_number = int(input("Enter a number to be convereted to binary : "))
		except ValueError: 
			print('Enter only digits, no characters or spaces. Try again')
		else: 
			return dec_number

def ask_for_more(): 
	'''
	This will ask user if he wants to continue
	'''

	while True: 
		cont = input('Do you want to convert more (y/n) : ')
		if cont.lower()[0] in 'yn': 
			return cont.lower()[0]
		print('Wrong choice. Use y to continue or n to quit')

def ask_for_conversion_type(): 
	'''
	This will ask user What type of conversion is required
	'''

	while True: 
		choice = input('What do you want to convert \n1. Binary to Decimal \n2. Decimal to Binary \n (1/2) : ')
		if choice[0] in '12': 
			return int(choice[0])
		print('Wrong choice. Enter 1 or 2 only')

def main(): 
	'''
	Main logic control
	'''
	do_more = 'y'

	while do_more == 'y': 
		answer = 0 
		if ask_for_conversion_type() == 1:
			answer = bin_to_dec(get_binary())
			print(f'Decimal value is {answer}')
		else: 
			answer = dec_to_bin(get_decimal())
			print(f'Binary value is {answer}')
		do_more = ask_for_more()

if __name__ == '__main__':
	main()




