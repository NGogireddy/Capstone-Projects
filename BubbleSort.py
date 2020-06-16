'''
This is a simple bubble sort algorithm
'''

def bubble_sort(numlist):
	'''
	Receiving the numbers to sort in a list
	'''

	print('List of entered numbers : {}'.format(numlist))
	length = len(numlist)
	index1 = 0

	while index1 < length: 
		index2 = index1+1
		while index2 < length: 
			if numlist[index2] < numlist[index1]: 
				numlist[index1],numlist[index2] = numlist[index2],numlist[index1]
			index2 += 1
		index1 += 1

	print('Sorted list of numbers is : {}'.format(numlist))

def main(): 
	'''
	Get the numbers from the users and call them for sort
	'''
	numlist = []
	while True: 
		try:
			numlist.append(int(input('Enter the number to sort or any character to quit : ')))
		except ValueError: 
			break
	bubble_sort(numlist)

if __name__ == '__main__':
	main()