'''
This module will be used to test the functionality of Credit Card Validator
'''

import unittest
import CreditCardValidator

class TestCreditCardValidator(unittest.TestCase):
	'''
	All unit test cases for the CreditCardValidator
	'''

	def test_check_start_invalid1(self): 
		'''
		Test with incorrect start digit 1 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(123)
		self.assertEqual(answer,False)

	def test_check_start_invalid2(self):
		'''
		Test with incorrect start digit 7 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(789)
		self.assertEqual(answer,False)

	def test_check_start_invalid3(self):
		'''
		Test with incorrect start digit 8 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(890)
		self.assertEqual(answer,False)

	def test_check_start_invalid4(self):
		'''
		Test with incorrect start digit 9 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(987)
		self.assertEqual(answer,False)

	def test_check_start_invalid5(self):
		'''
		Test with incorrect start digit 2 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(234)
		self.assertEqual(answer,False)

	def test_check_start_invalid6(self):
		'''
		Test with incorrect start digit 306 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(30601234567890)
		self.assertEqual(answer,False)

	def test_check_start_invalid6a(self):
		'''
		Test with correct start digit 305 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(30501234567890)
		self.assertEqual(answer,True)

	def test_check_start_invalid6b(self):
		'''
		Test with correct start digit 305 but invalid length for a card number
		'''
		answer = CreditCardValidator.check_starting_number(3050123456789)
		self.assertEqual(answer,False)

	def test_check_start_invalid6c(self):
		'''
		Test with incorrect start digit 305 but with invalid length for a card number
		'''
		answer = CreditCardValidator.check_starting_number(305012345678901)
		self.assertEqual(answer,False)

	def test_check_start_invalid7(self):
		'''
		Test with incorrect start digit 313 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(313)
		self.assertEqual(answer,False)

	def test_check_start_invalid8(self):
		'''
		Test with incorrect start digit 324 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(324)
		self.assertEqual(answer,False)

	def test_check_start_invalid9(self):
		'''
		Test with incorrect start digit 333 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(333)
		self.assertEqual(answer,False)

	def test_check_start_invalid10(self):
		'''
		Test with incorrect start digit 389 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(389)
		self.assertEqual(answer,False)

	def test_check_start_invalid11(self):
		'''
		Test with incorrect start digit 399 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(399)
		self.assertEqual(answer,False)

	def test_check_start_invalid12(self):
		'''
		Test with incorrect start digit 3514 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(3514)
		self.assertEqual(answer,False)

	def test_check_start_invalid13(self):
		'''
		Test with incorrect start digit 3527 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(3527)
		self.assertEqual(answer,False)

	def test_check_start_invalid13a(self):
		'''
		Test with correct start digit 3528 for a card number having 16 digits
		'''
		answer = CreditCardValidator.check_starting_number(3528123456781234)
		self.assertEqual(answer,True)

	def test_check_start_invalid13b(self):
		'''
		Test with correct start digit 3528 for a card number having 19 digits
		'''
		answer = CreditCardValidator.check_starting_number(3528123456781234123)
		self.assertEqual(answer,True)

	def test_check_start_invalid13c(self):
		'''
		Test with correct start digit 3589 for a card number having 17 digits
		'''
		answer = CreditCardValidator.check_starting_number(35891234567812341)
		self.assertEqual(answer,False)

	def test_check_start_invalid13d(self):
		'''
		Test with correct start digit 3589 for a card number having 18 digits
		'''
		answer = CreditCardValidator.check_starting_number(358912345678123412)
		self.assertEqual(answer,False)

	def test_check_start_invalid14(self):
		'''
		Test with incorrect start digit 3590 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(3590)
		self.assertEqual(answer,False)

	def test_check_start_invalid15(self):
		'''
		Test with incorrect start digit 3599 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(3599)
		self.assertEqual(answer,False)

	def test_check_start_invalid16(self):
		'''
		Test with incorrect start digit 5017 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5017)
		self.assertEqual(answer,False)

	def test_check_start_invalid17(self):
		'''
		Test with incorrect start digit 5019 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5019)
		self.assertEqual(answer,False)

	def test_check_start_invalid18(self):
		'''
		Test with incorrect start digit 5021 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5021)
		self.assertEqual(answer,False)

	def test_check_start_invalid19(self):
		'''
		Test with incorrect start digit 5037 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5037)
		self.assertEqual(answer,False)

	def test_check_start_invalid20(self):
		'''
		Test with incorrect start digit 5041 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5041)
		self.assertEqual(answer,False)

	def test_check_start_invalid20a(self):
		'''
		Test with correct start digit 5018 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5018123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid20b(self):
		'''
		Test with correct start digit 5020 and 17 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(50201234123412341)
		self.assertEqual(answer,False)

	def test_check_start_invalid20c(self):
		'''
		Test with correct start digit 5038 and 18 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(503812341234123412)
		self.assertEqual(answer,False)

	def test_check_start_invalid20d(self):
		'''
		Test with correct start digit 5893 and 19 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5893123412341234123)
		self.assertEqual(answer,True)

	def test_check_start_invalid20e(self):
		'''
		Test with correct start digit 51 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5100123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid20f(self):
		'''
		Test with correct start digit 52 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5200123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid20g(self):
		'''
		Test with correct start digit 53 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5300123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid20h(self):
		'''
		Test with correct start digit 54 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5400123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid20i(self):
		'''
		Test with correct start digit 55 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(5500123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid21(self):
		'''
		Test with incorrect start digit 560 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(560)
		self.assertEqual(answer,False)

	def test_check_start_invalid22(self):
		'''
		Test with incorrect start digit 6010 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6010)
		self.assertEqual(answer,False)

	def test_check_start_invalid22a(self):
		'''
		Test with correct start digit 6011 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6011123456781234)
		self.assertEqual(answer,True)

	def test_check_start_invalid22b(self):
		'''
		Test with correct start digit 6011 and 17 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(60111234567812341)
		self.assertEqual(answer,False)

	def test_check_start_invalid22c(self):
		'''
		Test with correct start digit 6011 and 18 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(601112345678123412)
		self.assertEqual(answer,False)

	def test_check_start_invalid22d(self):
		'''
		Test with correct start digit 6011 and 19 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6011123456781234123)
		self.assertEqual(answer,True)

	def test_check_start_invalid23(self):
		'''
		Test with incorrect start digit 6012 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6012)
		self.assertEqual(answer,False)

	def test_check_start_invalid24(self):
		'''
		Test with incorrect start digit 612 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(612)
		self.assertEqual(answer,False)

	def test_check_start_invalid25(self):
		'''
		Test with incorrect start digit 622125 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(622125)
		self.assertEqual(answer,False)

	def test_check_start_invalid25a(self):
		'''
		Test with correct start digit 622126 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6221261234123412)
		self.assertEqual(answer,True)

	def test_check_start_invalid25b(self):
		'''
		Test with correct start digit 622126 and 17 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(62212612341234123)
		self.assertEqual(answer,False)

	def test_check_start_invalid25c(self):
		'''
		Test with correct start digit 622925 and 18 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(622925123412341234)
		self.assertEqual(answer,False)

	def test_check_start_invalid25d(self):
		'''
		Test with correct start digit 622925 and 19 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6229251234123412341)
		self.assertEqual(answer,True)

	def test_check_start_invalid26(self):
		'''
		Test with incorrect start digit 622926 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(622926)
		self.assertEqual(answer,False)

	def test_check_start_invalid27(self):
		'''
		Test with incorrect start digit 636 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(636)
		self.assertEqual(answer,False)

	def test_check_start_invalid27a(self):
		'''
		Test with incorrect start digit 637 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6370123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid27b(self):
		'''
		Test with incorrect start digit 638 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6386123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid27c(self):
		'''
		Test with incorrect start digit 639 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6390123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid28(self):
		'''
		Test with incorrect start digit 643 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(643)
		self.assertEqual(answer,False)

	def test_check_start_invalid28a(self):
		'''
		Test with correct start digit 644 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6440123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid28b(self):
		'''
		Test with correct start digit 644 and 17 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(64401234123412341)
		self.assertEqual(answer,False)

	def test_check_start_invalid28c(self):
		'''
		Test with correct start digit 649 and 18 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(649012341234123412)
		self.assertEqual(answer,False)

	def test_check_start_invalid28d(self):
		'''
		Test with correct start digit 649 and 19 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6490123412341234123)
		self.assertEqual(answer,True)

	def test_check_start_invalid28e(self):
		'''
		Test with correct start digit 65 and 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6500123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid29(self):
		'''
		Test with incorrect start digit 660 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(660)
		self.assertEqual(answer,False)

	def test_check_start_invalid30(self):
		'''
		Test with incorrect start digit 6758 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6758)
		self.assertEqual(answer,False)

	def test_check_start_invalid30a(self):
		'''
		Test with incorrect start digit 6759 with 16 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6759123412341234)
		self.assertEqual(answer,True)

	def test_check_start_invalid30b(self):
		'''
		Test with incorrect start digit 6761 with 17 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(67611234123412341)
		self.assertEqual(answer,False)

	def test_check_start_invalid30c(self):
		'''
		Test with incorrect start digit 6762 with 18 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(676212341234123412)
		self.assertEqual(answer,False)

	def test_check_start_invalid30d(self):
		'''
		Test with incorrect start digit 6763 with 19 digits for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6763123412341234123)
		self.assertEqual(answer,True)

	def test_check_start_invalid31(self):
		'''
		Test with incorrect start digit 6764 for a card number
		'''
		answer = CreditCardValidator.check_starting_number(6764)
		self.assertEqual(answer,False)

	def test_verify_card_number1(self):
		'''
		Test to verify the card number is valid or not. Valid card1
		'''
		answer = CreditCardValidator.verify_card_number(4532732370590926)
		self.assertEqual(answer,True)
		
	def test_verify_card_number2(self):
		'''
		Test to verify the card number is valid or not. Valid card2
		'''
		answer = CreditCardValidator.verify_card_number(4532215424751526170)
		self.assertEqual(answer,True)
		
	def test_verify_card_number3(self):
		'''
		Test to verify the card number is valid or not. Valid card3
		'''
		answer = CreditCardValidator.verify_card_number(6011335299341614)
		self.assertEqual(answer,True)
		
	def test_verify_card_number4(self):
		'''
		Test to verify the card number is valid or not. Valid card4
		'''
		answer = CreditCardValidator.verify_card_number(6011399823450522029)
		self.assertEqual(answer,True)
		
	def test_verify_card_number5(self):
		'''
		Test to verify the card number is valid or not. Valid card5
		'''
		answer = CreditCardValidator.verify_card_number(30216345253401)
		self.assertEqual(answer,True)
		
	def test_verify_card_number6(self):
		'''
		Test to verify the card number is valid or not. Valid card6
		'''
		answer = CreditCardValidator.verify_card_number(30532492899568)
		self.assertEqual(answer,True)
		
	def test_verify_card_number7(self):
		'''
		Test to verify the card number is valid or not. Valid card7
		'''
		answer = CreditCardValidator.verify_card_number(4026517698321903)
		self.assertEqual(answer,True)
		
	def test_verify_card_number8(self):
		'''
		Test to verify the card number is valid or not. Valid card8
		'''
		answer = CreditCardValidator.verify_card_number(4913822983158002)
		self.assertEqual(answer,True)
		
	def test_verify_card_number9(self):
		'''
		Test to verify the card number is valid or not. Valid card9
		'''
		answer = CreditCardValidator.verify_card_number(5170757764785752)
		self.assertEqual(answer,True)
		
	def test_verify_card_number10(self):
		'''
		Test to verify the card number is valid or not. Valid card10
		'''
		answer = CreditCardValidator.verify_card_number(5167273744688590)
		self.assertEqual(answer,True)
		
	def test_verify_card_number11(self):
		'''
		Test to verify the card number is valid or not. Valid card11
		'''
		answer = CreditCardValidator.verify_card_number(3534311313874547)
		self.assertEqual(answer,True)
		
	def test_verify_card_number12(self):
		'''
		Test to verify the card number is valid or not. Valid card12
		'''
		answer = CreditCardValidator.verify_card_number(3529444897603680)
		self.assertEqual(answer,True)
		
	def test_verify_card_number13(self):
		'''
		Test to verify the card number is valid or not. Valid card13
		'''
		answer = CreditCardValidator.verify_card_number(3545796039213407072)
		self.assertEqual(answer,True)
		
	def test_verify_card_number14(self):
		'''
		Test to verify the card number is valid or not. Valid card14
		'''
		answer = CreditCardValidator.verify_card_number(36667431728389)
		self.assertEqual(answer,True)
		
	def test_verify_card_number15(self):
		'''
		Test to verify the card number is valid or not. Valid card15
		'''
		answer = CreditCardValidator.verify_card_number(36125108110142)
		self.assertEqual(answer,True)
		
	def test_verify_card_number16(self):
		'''
		Test to verify the card number is valid or not. Valid card16
		'''
		answer = CreditCardValidator.verify_card_number(6374785590638277)
		self.assertEqual(answer,True)
		
	def test_verify_card_number17(self):
		'''
		Test to verify the card number is valid or not. Valid card17
		'''
		answer = CreditCardValidator.verify_card_number(6398517428154074)
		self.assertEqual(answer,True)
		
	def test_verify_card_number18(self):
		'''
		Test to verify the card number is valid or not. Valid card18
		'''
		answer = CreditCardValidator.verify_card_number(371378385752994)
		self.assertEqual(answer,True)
		
	def test_verify_card_number19(self):
		'''
		Test to verify the card number is valid or not. Valid card19
		'''
		answer = CreditCardValidator.verify_card_number(342792523706702)
		self.assertEqual(answer,True)
		
	def test_verify_card_number20(self):
		'''
		Test to verify the card number is valid or not. Valid card20
		'''
		answer = CreditCardValidator.verify_card_number(345219998334155)
		self.assertEqual(answer,True)
		
	def test_verify_card_number21(self):
		'''
		Test to verify the card number is valid or not. Valid card21
		'''
		answer = CreditCardValidator.verify_card_number(5458399083406092)
		self.assertEqual(answer,True)
		
	def test_verify_card_number22(self):
		'''
		Test to verify the card number is valid or not. Valid card22
		'''
		answer = CreditCardValidator.verify_card_number(5584388993242082)
		self.assertEqual(answer,True)
		
	def test_verify_card_number23(self):
		'''
		Test to verify the card number is valid or not. Valid card23
		'''
		answer = CreditCardValidator.verify_card_number(6304052223157604)
		self.assertEqual(answer,True)
		
	def test_verify_card_number24(self):
		'''
		Test to verify the card number is valid or not. Valid card24
		'''
		answer = CreditCardValidator.verify_card_number(5018077162411125)
		self.assertEqual(answer,True)
		
	def test_verify_card_number25(self):
		'''
		Test to verify the card number is valid or not. Valid card25
		'''
		answer = CreditCardValidator.verify_card_number(6762620696606011)
		self.assertEqual(answer,True)
		
	def test_verify_card_number26(self):
		'''
		Test to verify the card number is valid or not. Invalid card26
		'''
		answer = CreditCardValidator.verify_card_number(4539173530495786)
		self.assertEqual(answer,False)
		
	def test_verify_card_number27(self):
		'''
		Test to verify the card number is valid or not. Invalid card27
		'''
		answer = CreditCardValidator.verify_card_number(6011399823450522027)
		self.assertEqual(answer,False)
		
	def test_verify_card_number28(self):
		'''
		Test to verify the card number is valid or not. Invalid card28
		'''
		answer = CreditCardValidator.verify_card_number(30532492899560)
		self.assertEqual(answer,False)
		
	def test_verify_card_number29(self):
		'''
		Test to verify the card number is valid or not. Invalid card29
		'''
		answer = CreditCardValidator.verify_card_number(5170757764785759)
		self.assertEqual(answer,False)
		
	def test_verify_card_number30(self):
		'''
		Test to verify the card number is valid or not. Invalid card30
		'''
		answer = CreditCardValidator.verify_card_number(6762620696606018)
		self.assertEqual(answer,False)
		

if __name__ == '__main__':
	unittest.main()