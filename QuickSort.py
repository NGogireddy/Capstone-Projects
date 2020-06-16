'''
Program to get some numbers and sort them using quick sort algorigthm.
'''

NUMBERS = []

def partition(low,high): 
	'''
	Sorts the numbers between low and high index of NUMBERS array. 
	'''

	global NUMBERS

	low_index = low  # Keeps track of the smaller numbers
	big_index = low  # keeps track of the bigger numbers than pivot
	pivot = NUMBERS[high]
	while big_index < high: 
		if NUMBERS[big_index] < pivot: 
			NUMBERS[low_index],NUMBERS[big_index] = NUMBERS[big_index],NUMBERS[low_index]
			low_index += 1
		big_index += 1
	NUMBERS[high],NUMBERS[low_index] = NUMBERS[low_index],NUMBERS[high]
	return low_index

def quick_sort(low,high): 
	'''
	Partitions the array and calls the quick sort on the left and right wings
	'''

	global NUMBERS

	if low<high: 
		pivot = partition(low,high)
		
		quick_sort(low,pivot-1)
		quick_sort(pivot+1,high)

def main(): 
	'''
	Gets the numbers from the users and call the sort. 
	'''

	global NUMBERS

	while True: 
		try:
			NUMBERS.append(int(input('Enter the number to sort or any character to stop : ')))
		except ValueError:
			break

	print(f'Numbers entered are {NUMBERS}')
	quick_sort(0,len(NUMBERS)-1)
	print(f'After sorting list is {NUMBERS}')

if __name__ == '__main__':
	main()
