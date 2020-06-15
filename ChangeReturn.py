'''
This program give the denomination of the change to be tendered.
Note: Input is taken in whole numbers (pence) to ensure accuracy. i.e., £2 should be entered as 200
By the way the code is to handle the change in UK currency. 
Following are the denominations considered for the program. 
£20, £10, £5, £2, £1, 50p, 20p, 10p, 5p, 2p, 1p
'''

CURRENCY = (2000,1000,500,200,100,50,20,10,5,2,1)
LABEL = ('£20','£10','£5','£2','£1','50p','20p','10p','5p','2p','1p')

def tender_change(payment,cost): 
	'''
	Takes the payment,cost as input and returns a list of change to be returned
	'''

	answer = [0,0,0,0,0,0,0,0,0,0,0]
	change = payment-cost
	index = 0

	while index<len(CURRENCY):

		while change >= CURRENCY[index]: 
			answer[index] += 1
			change -= CURRENCY[index]

		index += 1

	return(answer)

def print_tender(denomination): 
	'''
	Prints the change in a readable format
	'''
	change = 0
	print('{0:11} | {1:7} | {2:7}'.format('Denomination ','Number ','Value '))
	for index,num in enumerate(denomination): 
		if num>0: 
			print('{0:13} * {1:^7} = {2:>7}'.format(LABEL[index] , str(denomination[index]) , str(CURRENCY[index]*denomination[index])))
			change += CURRENCY[index]*denomination[index]

	print('{0:23} = {1:>8}'.format('Total Change ',str(change)+'p'))

def main(): 
	'''
	Main program to ask the cost price and payment amount, calls the function that prints the change
	'''

	while True:
		try: 
			cost = int(input('Enter the cost of the purchase in pence (eg £10.05p should be entered as 1005) :'))
		except ValueError:
			print('Enter value in numbers. No special characters allowed. For £14.00p enter 1400. Try again')
		else:
			if cost <= 0: 
				print('Cost of an item cannot be zero or lesser. Try again')
			else: 
				break 

	while True:
		try: 
			cash = int(input('Enter the cash received for the purchase in pence (eg £10 should be entered as 1000) :'))
		except ValueError:
			print('Enter value in numbers. No special characters allowed. For £1p enter 100. Try again')
		else:
			if cash < cost: 
				print('Cash given cannot be less than the cost of the item. Try again')
			else: 
				break

	print(f'Cash recieved is {cash}. Cost of the item is {cost}. Change to return is {cash-cost}. Denomination given below.')
	print_tender(tender_change(cash,cost))

if __name__ == '__main__':
	main()
