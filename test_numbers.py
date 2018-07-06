import unittest
from sys import stdin, stdout
from numbers import RandomNumberGenerator

class RandomNumberGeneratorTesting(unittest.TestCase):
	def test_input_domains(self):
		rng = RandomNumberGenerator()
		rng_values = rng.get_values()

		# value checking for num_testcases
		value_error_values_num_testcases = [-2, 0]
		[self.assertRaises(ValueError, rng.store_num_testcases, i) for i in value_error_values_num_testcases]
		
		# value checking for print_num_testcases
		value_error_values_print_num_testcases = '@Qr|'
		[self.assertRaises(ValueError, rng.store_print_num_testcases, i) for i in value_error_values_print_num_testcases]

		# value checking for is_float
		value_error_values_is_float = '#Rv"'
		[self.assertRaises(ValueError, rng.store_is_float, i) for i in value_error_values_is_float]

		# value checking for minvlaue and maxvalue
		value_error_values_min_and_max_values = [[0, 0], [7, 5], [-5, -7], [0, -2]]
		[self.assertRaises(ValueError, rng.store_minvalue_and_maxvalue, i) for i in value_error_values_min_and_max_values]

	def test_input_types(self):
		rng = RandomNumberGenerator()
		rng_values = rng.get_values()

		# type checking for num_testcase
		type_error_values_num_testcases = [4.5, True]
		[self.assertRaises(TypeError, rng.store_num_testcases, i) for i in type_error_values_num_testcases]

		# type checking for minvalue and maxvalue
		type_error_values_minvalue_and_maxvalue = [[2.0, 15.0], [-10.0, -15.0], [-15.0, -13.0], [True, 1], [False, True], [False, 2]]
		[self.assertRaises(TypeError, rng.store_minvalue_and_maxvalue, i) for i in type_error_values_minvalue_and_maxvalue]