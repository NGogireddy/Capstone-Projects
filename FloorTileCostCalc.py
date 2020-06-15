'''
Module to calculate the cost of tiles in flooring
'''

def cost_calc(length,width,cost): 
	return length*width*cost

def main(): 
	'''
	get length width and cost
	'''
	while True:
		try:
			length=float(input('Enter the length :'))
		except ValueError: 
			print('Enter length in numbers only. Try again')
		else: 
			if length <= 0: 
				print('Length cannot be less than 0. Try again')
			else:
				break
	while True:
		try:
			width=float(input('Enter the width :'))
		except ValueError: 
			print('Enter width in numbers only. Try again')
		else: 
			if width <= 0: 
				print('Width cannot be less than 0. Try again')
			else:
				break
	while True:
		try:
			cost=float(input('Enter the cost :'))
		except ValueError: 
			print('Enter cost in numbers only. Try again')
		else: 
			if cost <= 0: 
				print('Cost cannot be less than 0. Try again')
			else:
				break

	print('Cost for laying the floor of length : {} and width : {} is {}'.format(length,width,cost_calc(length,width,cost)))

if __name__ == '__main__':
	main()