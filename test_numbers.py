import unittest
from sys import stdin, stdout
from numbers import RandomNumberGenerator

class RandomNumberGeneratorTesting(unittest.TestCase):
	def test_values(self):
		self.rng = RandomNumberGenerator()
		rng_values = self.rng.get_values()

		self.assertLess(0, rng_values["num_testcases"])
		possible_print_num_testcases = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']
		self.assertIn(rng_values['print_num_testcases'], possible_print_num_testcases)
		self.assertIn(rng_values["options"]["is_float"], possible_print_num_testcases)

		self.assertLess(rng_values["options"]["minvalue"], rng_values['options']["maxvalue"])
		