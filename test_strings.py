import unittest
from strings import RandomStringGenerator, get_distinct_letters, get_random_letters
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

	def test_input_types(self):
		rsg = RandomStringGenerator()

		# type checking for num_testcase
		type_error_values_num_testcases = [4.5, True]
		[self.assertRaises(TypeError, rsg.store_num_testcases, i) for i in type_error_values_num_testcases]

		# type checking for print_num_testcases
		type_error_values_print_num_testcases = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rsg.store_print_num_testcases, i) for i in type_error_values_num_testcases]

		# type checking for string_size
		type_error_values_string_size = [4.5, True]
		[self.assertRaises(TypeError, rsg.store_string_size, i) for i in type_error_values_string_size]

		# type checking for print_string_size
		type_error_values_print_string_size = [4, 5.5 , True, 3+4j]
		[self.assertRaises(TypeError, rsg.store_print_string_size, i) for i in type_error_values_print_string_size]

		# type checking for distinct
		type_error_values_distinct = [4, 5.5, True, 3.4j]
		[self.assertRaises(TypeError, rsg.store_distinct, i) for i in type_error_values_distinct]

		# type checking for allowed
		type_error_values_allowed = [3+4j, True, 5.55]
		[self.assertRaises(TypeError, rsg.store_allowed, i) for i in type_error_values_allowed]

	def test_output(self):
		rsg = RandomStringGenerator()

		# checking for distinct letters output
		output_error_values = [[rsg.values['possible_letters'], 10], [rsg.values['possible_letters'] ,58]]
		for possible_letters, string_size in output_error_values:
			# for distinct letters 
			ans = get_distinct_letters(possible_letters, string_size)
			freq = {}
			for i in ans:
				if freq.has_key(i):
					freq[i] += 1
				else:
					freq[i] = 1

			# checking if occurence is only 1 or not
			[self.assertEqual(1, value) for value in freq.values()]
			# checking whether all letters are in possible_letters or not
			[self.assertIn(letter, possible_letters) for letter in ans]


			# checking for random letters output
			ans = get_random_letters(possible_letters, string_size)
			# checking whether all letters are in possible_letters or not
			[self.assertIn(letter, possible_letters) for letter in ans]