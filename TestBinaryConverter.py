# This is to test the methods in BinaryConverter module

import unittest
import BinaryConverter

class TestBinCoverter(unittest.TestCase):
	'''
	Test class to test methods in Binary Converter python module
	'''

	def test_bin_to_decimal1(self): 
		'''
		Testing binary number 0
		'''
		answer = BinaryConverter.bin_to_dec('0')
		self.assertEqual(answer,0)

	def test_bin_to_decimal2(self): 
		'''
		Testing binary number 1
		'''
		answer = BinaryConverter.bin_to_dec('1')
		self.assertEqual(answer,1)

	def test_bin_to_decimal3(self): 
		'''
		Testing binary number 1
		'''
		answer = BinaryConverter.bin_to_dec('10')
		self.assertEqual(answer,2)

	def test_bin_to_decimal4(self): 
		'''
		Testing binary number 1
		'''
		answer = BinaryConverter.bin_to_dec('01')
		self.assertEqual(answer,1)

	def test_bin_to_decimal5(self): 
		'''
		Testing binary number 1
		'''
		answer = BinaryConverter.bin_to_dec('11')
		self.assertEqual(answer,3)

	def test_bin_to_decimal6(self): 
		'''
		Testing binary number 1
		'''
		answer = BinaryConverter.bin_to_dec('100')
		self.assertEqual(answer,4)

	def test_bin_to_decimal7(self): 
		'''
		Testing binary number 1
		'''
		answer = BinaryConverter.bin_to_dec('110')
		self.assertEqual(answer,6)

	def test_dec_to_binary1(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(0)
		self.assertEqual(answer,'0')

	def test_dec_to_binary2(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(1)
		self.assertEqual(answer,'1')

	def test_dec_to_binary3(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(2)
		self.assertEqual(answer,'10')

	def test_dec_to_binary4(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(3)
		self.assertEqual(answer,'11')

	def test_dec_to_binary5(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(8)
		self.assertEqual(answer,'1000')

	def test_dec_to_binary6(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(10)
		self.assertEqual(answer,'1010')

	def test_dec_to_binary7(self): 
		'''
		Testing decimal number 1
		'''
		answer = BinaryConverter.dec_to_bin(15)
		self.assertEqual(answer,'1111')

if __name__ == '__main__':
	unittest.main()

