import unittest
from sys import stdin, stdout
from arrays import RandomArrayGenerator

class RandomArrayGeneratorTesting(unittest.TestCase):
	def test_values(self):
		self.rag = RandomArrayGenerator()
		rag_values = self.rag.get_values()

		self.assertLess(0, rag_values['num_testcases'])

		possible_print_num_testcases = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']
		self.assertIn(rag_values['print_num_testcases'], possible_print_num_testcases)

		self.assertLess(0, rag_values['options']['array_size'])

		self.assertIn(rag_values['options']['print_array_size'], possible_print_num_testcases)
		self.assertIn(rag_values['options']['distinct'], possible_print_num_testcases)
		self.assertIn(rag_values['options']['strictly_increasing'], possible_print_num_testcases)

		self.assertLess(rag_values["options"]["minvalue"], rag_values['options']["maxvalue"])
		if rag_values['options']['distinct'] in possible_print_num_testcases[:4] or rag_values['options']['strictly_increasing'] in possible_print_num_testcases[:4]:
			self.assertLess(rag_values['options']['array_size'], rag_values['options']['maxvalue'] - rag_values['options']['minvalue'] + 1)
