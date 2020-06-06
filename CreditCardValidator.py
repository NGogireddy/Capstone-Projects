# Thie program gets a credit card number from user and verifies if it is valid or not
'''
This program does an indetailed verification on the credit card number range. 
The source for valid credit card numbers is taken from 
https://www.freeformatter.com/credit-card-number-generator-validator.html
The logic to validate a card number is referred in Wikipedia
https://en.wikipedia.org/wiki/Luhn_algorithm
This code is written on 06/06/2020

PS: I have some confusion over credit card range for mastercards starting with 2, hence ignored them in validation
'''

INVALID_START_NUMBER = '012789'

def get_card_number():
	'''
	Ask a card number to the user. Only verifies if it is a number
	'''

	while True:
		try: 
			number = int(input('Enter a card number to validate : '))
		except ValueError:
			print('Enter a valid number without any spaces')
			continue
		if number <= 0: 
			print('Enter a positive number')
			continue
		return number

def check_starting_number(number):
	'''
	This will check if the starting digit and the total number of digits are valid
	'''
	char_number = str(number)

	if char_number[0] in INVALID_START_NUMBER:
		print('Card number is invalid. It cannot start with 0/1/2/7/8/9')
		return False
	elif ((char_number[0:2] == '34' or 
		char_number[0:2] == '37') and 
		len(char_number) == 15): 
		print('This might be an Amex card')
		return True
	elif ((char_number[0:2] == '36') or 
		  (char_number[0:2] == '30' and
		   int(char_number[2]) <= 5) and
		  len(char_number) == 14): 
		print('This might be an Diners Club card')
		return True
	elif ((char_number[0:2] == '35' and
		   28 <= int(char_number[2:4]) <= 89) and
		   (len(char_number) == 16 or len(char_number) == 19)): 
		print('This might be an JCB card')
		return True
	elif ((char_number[0] == '4') and
		  (len(char_number) == 13 or 
		  	len(char_number) == 16 or 
		  	len(char_number) == 19)):
		print('This might be a Visa/Visa Electron Card')
		return True
	elif ((51 <= int(char_number[0:2]) <= 55) and len(char_number) == 16): 
		print('This might be a Master Card')
		return True
	elif ((char_number[0:4] == '5018' or 
		char_number[0:4] == '5020' or 
		char_number[0:4] == '5038' or 
		char_number[0:4] == '5893') and 
		(len(char_number) == 16 or len(char_number) == 19)):
		print('This might be a Maestro card')
		return True
	elif ((char_number[0:4] == '6011' or 
		char_number[0:2] == '65' or 
	    ((char_number[0:3] == '622') and (126 <= int(char_number[3:6]) <= 925)) or
		644 <= int(char_number[0:3]) <= 649) and 
		(len(char_number) == 16 or len(char_number) == 19)):
		print('This might be Discover card')
		return True
	elif ((char_number[0:3] == '637' or 
		char_number[0:3] == '638' or
		char_number[0:3] == '639') and 
		len(char_number) == 16):
		print('This might be a Instapay card')
		return True
	elif ((char_number[0:4] == '6304' or
		char_number[0:4] == '6759' or
		char_number[0:4] == '6761' or
		char_number[0:4] == '6762' or
		char_number[0:4] == '6763') and 
		(len(char_number) == 16 or len(char_number) == 19)):
		print('This might be a Maestro card')
		return True
	return False
	


def verify_card_number(number):
	'''
	This will do the actual validation on the card number. 
	'''
	char_number = str(number)
	last_digit = int(char_number[-1])
	rev_number = char_number[-2::-1]
	sum = 0 
	for a,b in enumerate(rev_number):
		# Double the value of digits in odd places, less 9 if value > 9 and sum up all digits
		digit = int(b)
		if a%2 == 0: 
			digit *= 2
			if digit >= 10:
				digit -= 9
		sum += digit
	if (sum*9)%10 == last_digit:
		return True 
	else:
		return False

def main():
	'''
	This is the main module. 
	Gets the number from user
	Verifies the carrier and their first digits
	'''

	card_num = get_card_number()
	if check_starting_number(card_num):
		if (verify_card_number(card_num)):
			print('Card number is valid')
		else:
			print('Card number is invalid')
	else:
		print('Card number is invalid')

if __name__ == '__main__':
	main()

