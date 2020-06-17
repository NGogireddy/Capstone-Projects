'''
Checks if the string is pallindrome.
PS: Checks are case insensitive. ie 'Tat' is pallindrome.
'''

def main(): 
	string = input('Enter the string to check if that is pallindrome : ')
	if string.lower() == string[-1::-1].lower():
		print(f'{string} is pallindrome')
	else:
		print(f'{string} is not pallindrome')

if __name__ == '__main__':
	main()