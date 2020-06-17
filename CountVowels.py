'''
Solution to count the vowels in a string and report them by each letter
'''

def main(): 

	vowels = ['a','e','i','o','u']
	string = input('Enter the string for vowel report : ')

	vowel_count = [0,0,0,0,0]

	for index,char in enumerate(vowels): 
		vowel_count[index] = string.lower().count(char) 

	print('A total of {} vowels found. Summary below.'.format(sum(vowel_count)))
	for char,count in zip(vowels,vowel_count): 
		print("Count of '{}'  : {}".format(char,count))

if __name__ == '__main__':
	main()
