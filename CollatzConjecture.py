'''
This is the solution to Collatz conjecture. Collatz conjecture is to findout the number of steps needed for a number to reach 1. 
Following are the rules. 
1. If the number is even divide by 2
2. If the number is odd multiply by 3 and add 1

Demonstration for 6. 

step1 : 6/2 --> 3
step2 : 3*3+1 --> 10
step3 : 10/2 --> 5
step4 : 5*3+1 --> 16
step5 : 16/2 --> 8 
step6 : 8/2 --> 4
step7 : 4/2 --> 2
step8 : 2/2 --> 1

It takes 8 steps to reach 1 for number 6

'''

def count_steps(number):
	'''
	Main logic to apply the steps and reach 1, keep a track of steps and return it.
	'''

	steps = 0
	if number == 1: 
		return 0
	while number>1: 
		if number%2 == 0:
			number = int(number/2)
		else:
			number = number*3 + 1
		steps += 1
	return(steps)

def main(): 
	'''
	Main logic to get the number and print the answer
	'''
	while True:
		try:
			number = int(input('Enter a positive number to check the steps for reaching 1 : '))
		except ValueError: 
			print('Enter only positive numbers. Try again')
		else: 
			if number <= 0: 
				print('Enter only positive numbers > 0 ')
			else: 
				break
	
	print('We need {} steps to reach 1 for the number {}'.format(count_steps(number),number))

if __name__ == '__main__':
	main()