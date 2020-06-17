'''
Solution to pig latin problem. 
Rules: Take all the consonents before the first vowel and put them at the end. Add 'ay' to it.
If word starts with a vowel. Just add 'yay' to the word. No re-org. 
If workd has not vowels add 'ay' to the end

Examples: 

Cast --> Astcay
Chase --> Asechay
Every --> Everyyay
Myth --> Mythay

'''

def main(): 

	vowels = 'aeiou'

	string = input('Enter the word you want to convert in Pig Latin : ')
	piglatin_string = ''

	if string[0].lower() in vowels: 
		piglatin_string = string + 'ay'
	else:
		index = 1
		while index < len(string):
			if string[index].lower() in vowels: 
				break
			index += 1
		if index < len(string): 
			piglatin_string = string[index:] + string[0:index] + 'ay'
		else: 
			piglatin_string = string + 'ay'

	print('Word entered is {0:10} : {1:}'.format(' ',string))
	print('Pig Latin conversion is {0:2} : {1:}'.format(' ',piglatin_string))

if __name__ == '__main__':
	main()