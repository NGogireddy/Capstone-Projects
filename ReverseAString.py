'''
prints the string entered by the user in reverse order
'''

def main(): 
	string = input('Enter a string you want to see reversed : ')
	print('String entered is {0:4} : {1:}'.format(' ',string))
	print('String reveresed is {0:2} : {1:}'.format(' ',string[-1::-1]))

if __name__ == '__main__':
	main()
