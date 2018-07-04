import unittest
from sys import stdin, stdout
from numbers import RandomNumberGenerator

class RandomNumberGeneratorTesting(unittest.TestCase):
	def test_values(self):
		self.rng = RandomNumberGenerator()
		self.rng_values = self.rng.get_values()

		possible_print_num_testcases = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']
		self.assertIn(self.rng_values['print_num_testcases'], possible_print_num_testcases)
		self.assertIn(self.rng_values["options"]["is_float"], possible_print_num_testcases)

		self.assertLess(self.rng_values["options"]["minvalue"], self.rng_values['options']["maxvalue"])
		