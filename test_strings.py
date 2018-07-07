import unittest
from sys import stdin, stdout
from strings import RandomStringGenerator
import string

class RandomStringGeneratorTesting(unittest.TestCase):
	def test_input_domains(self):
		rsg = RandomStringGenerator()

		# value checking for num_testcases
		value_error_values_num_testcases = [-2, 0]
		[self.assertRaises(ValueError, rsg.store_num_testcases, i) for i in value_error_values_num_testcases]
		
		# value checking for print_num_testcases
		value_error_values_print_num_testcases = '@Qr|'
		[self.assertRaises(ValueError, rsg.store_print_num_testcases, i) for i in value_error_values_print_num_testcases]

		# value checking for string size
		value_error_values_string_size = [-2, 0]
		[self.assertRaises(ValueError, rsg.store_string_size, i) for i in value_error_values_string_size]
		
		# value checking for print_string_size
		value_error_values_print_string_size = '@Qr|'
		[self.assertRaises(ValueError, rsg.store_print_string_size, i) for i in value_error_values_print_string_size]

		# value checking for distinct
		value_error_values_distinct = '@Qr|'
		[self.assertRaises(ValueError, rsg.store_distinct, i) for i in value_error_values_distinct]

		value_error_values_allowed = ['yyyyn', 'yyxx', 'yyyx', 'nnnz', 'yyy', 'xxx', 'nnnn']
		[self.assertRaises(ValueError, rsg.store_allowed, i) for i in value_error_values_allowed]