import unittest
from sys import stdin, stdout
from numbers import RandomNumberGenerator, get_random_integer, get_random_float

class RandomNumberGeneratorTesting(unittest.TestCase):
	def test_input_domains(self):
		rng = RandomNumberGenerator()

		# value checking for num_testcases
		value_error_values_num_testcases = [-2, 0]
		[self.assertRaises(ValueError, rng.store_num_testcases, i) for i in value_error_values_num_testcases]
		
		# value checking for print_num_testcases
		value_error_values_print_num_testcases = '@Qr|'
		[self.assertRaises(ValueError, rng.store_print_num_testcases, i) for i in value_error_values_print_num_testcases]

		# value checking for is_float
		value_error_values_is_float = '#Rv"'
		[self.assertRaises(ValueError, rng.store_is_float, i) for i in value_error_values_is_float]

		# value checking for minvalue and maxvalue
		value_error_values_min_and_max_values = [[0, 0], [7, 5], [-5, -7], [0, -2], [10, 10]]
		[self.assertRaises(ValueError, rng.store_minvalue_and_maxvalue, i) for i in value_error_values_min_and_max_values]

	def test_input_types(self):
		rng = RandomNumberGenerator()

		# type checking for num_testcase
		type_error_values_num_testcases = [4.5, True]
		[self.assertRaises(TypeError, rng.store_num_testcases, i) for i in type_error_values_num_testcases]

		# type checking for print_num_testcases
		type_error_values_print_num_testcases = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rng.store_print_num_testcases, i) for i in type_error_values_print_num_testcases]

		# type checking for distinct
		type_error_values_is_float = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rng.store_is_float, i) for i in type_error_values_is_float]

		# type checking for minvalue and maxvalue
		type_error_values_minvalue_and_maxvalue = [[0.5, 1.2], [2.0, 15.0], [-10.0, -15.0], [-15.0, -13.0], [True, 1], [False, True], [False, 2]]
		[self.assertRaises(TypeError, rng.store_minvalue_and_maxvalue, i) for i in type_error_values_minvalue_and_maxvalue]

	def test_output(self):
		rng = RandomNumberGenerator()

		# checking random float values
		output_error_values_minvalue_and_maxvalue = [[-10, -5], [-7, -6], [6, 7], [0, 1], [4, 5], [-1, 0]]
		for i in output_error_values_minvalue_and_maxvalue:
			# check for both random float and random int between give window
			random_float = get_random_float(i[0], i[1])
			self.assertLessEqual(random_float, i[1])
			self.assertGreaterEqual(random_float, i[0])

			random_int = get_random_integer(i[0], i[1])
			self.assertLessEqual(random_int, i[1])
			self.assertGreaterEqual(random_int, i[0])