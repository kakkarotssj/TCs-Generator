import unittest
from sys import stdin, stdout
from arrays import RandomArrayGenerator

class RandomArrayGeneratorTesting(unittest.TestCase):
	def test_values(self):
		self.rag = RandomArrayGenerator()
		self.rag_values = self.rag.get_values()

		self.assertLess(0, self.rag_values['num_testcases'])

		possible_print_num_testcases = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']
		self.assertIn(self.rag_values['print_num_testcases'], possible_print_num_testcases)

		self.assertLess(0, self.rag_values['options']['array_size'])

		self.assertIn(self.rag_values['options']['print_array_size'], possible_print_num_testcases)
		self.assertIn(self.rag_values['options']['distinct'], possible_print_num_testcases)
		self.assertIn(self.rag_values['options']['strictly_increasing'], possible_print_num_testcases)

		self.assertLess(self.rag_values["options"]["minvalue"], self.rag_values['options']["maxvalue"])
		if self.rag_values['options']['distinct'] in possible_print_num_testcases[:4] or self.rag_values['options']['strictly_increasing'] in possible_print_num_testcases[:4]:
			self.assertLess(self.rag_values['options']['array_size'], self.rag_values['options']['maxvalue'] - self.rag_values['options']['minvalue'] + 1)
