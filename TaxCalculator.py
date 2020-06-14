'''
This module will calculate the tax of an item in various countries and/or states
Note: The countries/states within US and tax slabs are predefined.
'''

TAXES = {'Countries':{'UK':20,'ESP':21,'GER':19,'JAP':8,'CAN':5},
'States':{'FL':7,'NY':20,'AZ':5.6,'TX':6.25,'MT':0}}

def get_choice(): 
	'''
	Gets the choice from the user country or state
	'''
	while True: 
		choice = input('Select a choice\n1. Country\n2. State\n (1/2): ')
		if choice[0] in '12': 
			return(int(choice[0]))
		else: 
			print('Enter numbers only and either 1 or 2. Try Again')

def get_country(): 
	'''
	Gets the country of users choice
	'''
	while True:
		country = input('Select a country from '+','.join(TAXES['Countries'].keys())+' ')
		if country.upper() in TAXES['Countries'].keys():
			return country.upper()
		else: 
			print('Wrong input. Try again')

def get_state(): 
	'''
	Getst the state of users choice
	'''
	while True: 
		state = input('Select a state from '+','.join(TAXES['States'].keys())+' ')
		if state.upper() in TAXES['States'].keys():
			return state.upper()
		else: 
			print('Wrong input. Try again')

def get_amount():
	'''
	Gets the amount for which tax need to be calculated
	'''
	while True: 
		try:
			amount = float(input('Enter the amount to calculate tax :'))
		except ValueError:
			print('Entered value is not a number. Try again only numbers and dots are allowed')
		else:
			return amount

def add_tax(amount,tax): 
	'''
	Calculates the tax and adds it to the amount before returning the value 
	'''
	return float(amount)+float(amount*tax/100)

def main():
	'''
	Controls the main logic of the program. 
	'''
	amount= get_amount()
	choice = get_choice()
	if choice == 1: 
		country = get_country()
		answer = add_tax(amount,TAXES['Countries'][country])
		print(f'Value after tax for {amount} in {country} is {answer}')
	else:
		state = get_state()
		answer = add_tax(amount,TAXES['States'][state])
		print(f'Value after tax for {amount} in {state} is {answer}')

if __name__ == '__main__':
	main()