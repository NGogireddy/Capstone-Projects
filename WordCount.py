'''
Counts the words in a file
'''

def main(): 
	'''
	Get the full file name along with the path
	'''
	fname = input('Please enter the file name with full path : ')

	try: 
		with open(fname,mode='r') as file: 
			text = file.read()
			word_list = text.replace('\n',' ').split(' ')
			print(word_list)
			print(f'Total words in the file {len(word_list)}')

	except FileNotFoundError:
		print('Incorrect file path/name.')

if __name__ == '__main__':
	main()

