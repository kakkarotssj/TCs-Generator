import unittest
from sys import stdin, stdout
from arrays import RandomArrayGenerator

class RandomArrayGeneratorTesting(unittest.TestCase):
	def test_values(self):
		rag = RandomArrayGenerator()

		# value checking for num_testcases
		value_error_values_num_testcases = [-2, 0]
		[self.assertRaises(ValueError, rag.store_num_testcases, i) for i in value_error_values_num_testcases]
		
		# value checking for print_num_testcases
		value_error_values_print_num_testcases = '@Qr|'
		[self.assertRaises(ValueError, rag.store_print_num_testcases, i) for i in value_error_values_print_num_testcases]

		# value checking for array_size
		value_error_values_array_size = [-2, 0]
		[self.assertRaises(ValueError, rag.store_array_size, i) for i in value_error_values_array_size]
		
		# value checking for print_array_size
		value_error_values_print_array_size = '@Qr|'
		[self.assertRaises(ValueError, rag.store_print_array_size, i) for i in value_error_values_print_array_size]

		# value checking for strictly_increasing
		value_error_values_strictly_increasing = '@Qr|'
		[self.assertRaises(ValueError, rag.store_strictly_increasing, i) for i in value_error_values_strictly_increasing]

		# value checking for distinct
		value_error_values_distinct = '@Qr|'
		[self.assertRaises(ValueError, rag.store_distinct, i) for i in value_error_values_distinct]

		# value checking for minvalue and maxvalue
		value_error_values_min_and_max_values = [[0, 0], [7, 5], [-5, -7], [0, -2], [10, 10]]
		[self.assertRaises(ValueError, rag.store_minvalue_and_maxvalue, [i, rag.values]) for i in value_error_values_min_and_max_values]

	def test_input_types(self):
		rag = RandomArrayGenerator()

		# type checking for num_testcase
		type_error_values_num_testcases = [4.5, True]
		[self.assertRaises(TypeError, rag.store_num_testcases, i) for i in type_error_values_num_testcases]

		# type checking for print_num_testcases
		type_error_values_print_num_testcases = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rag.store_print_num_testcases, i) for i in type_error_values_print_num_testcases]

		# type checking for array_size
		type_error_values_array_size = [4.5, True]
		[self.assertRaises(TypeError, rag.array_size, i) for i in type_error_values_array_size]

		# type checking for print_array_size
		type_error_values_print_array_size = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rag.store_print_array_size, i) for i in type_error_values_print_array_size]

		# type checking for strictly_increasing
		type_error_values_strictly_increasing = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rag.store_strictly_increasing, i) for i in type_error_values_strictly_increasing]

		# type checking for distinct
		type_error_values_distinct = [4, 5.5, True, 3+4j]
		[self.assertRaises(TypeError, rag.store_distinct, i) for i in type_error_values_distinct]

		# type checking for minvalue and maxvalue
		type_error_values_minvalue_and_maxvalue = [[0.5, 1.2], [2.0, 15.0], [-10.0, -15.0], [-15.0, -13.0], [True, 1], [False, True], [False, 2], [3+4j, True]]
		[self.assertRaises(TypeError, rag.store_minvalue_and_maxvalue, [i, rag.values]) for i in type_error_values_minvalue_and_maxvalue]