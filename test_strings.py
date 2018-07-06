import unittest
from sys import stdin, stdout
from strings import RandomStringGenerator
import string

class RandomStringGeneratorTesting(unittest.TestCase):
	def test_values(self):
		self.rsg = RandomStringGenerator()
		rsg_values = self.rsg.get_values()

		self.assertLess(0, rsg_values['num_testcases'])

		possible_print_num_testcases = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']
		self.assertIn(rsg_values['print_num_testcases'], possible_print_num_testcases)

		self.assertLess(0, rsg_values['options']['string_size'])
		self.assertIn(rsg_values['options']['print_string_size'], possible_print_num_testcases)

		self.assertIn(rsg_values['options']['distinct'], possible_print_num_testcases)

		self.assertEqual(len(rsg_values['options']['allowed']), 4)
		for y_n in rsg_values['options']['allowed']:
			self.assertIn(y_n, possible_print_num_testcases)

		possible_letters = ''
		for i in range(4):
			if i == 0 and rsg_values['options']['allowed'][0] in ['T', 't', 'y', 'Y']:
				possible_letters += string.uppercase
			elif i == 1 and rsg_values['options']['allowed'][1] in ['T', 't', 'y', 'Y']:
				possible_letters += string.lowercase
			elif i == 2 and rsg_values['options']['allowed'][2] in ['T', 't', 'y', 'Y']:
				possible_letters += string.digits
			elif i == 3 and rsg_values['options']['allowed'][3] in ['T', 't', 'y', 'Y']:
				possible_letters += string.punctuation

		if rsg_values['options']['distinct'] in possible_print_num_testcases[:4]:
			self.assertLessEqual(rsg_values['options']['string_size'], len(possible_letters))
		
