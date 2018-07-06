import random
from sys import stdin, stdout

class RandomNumberGenerator:
	def __init__(self):
		self.values = {}
		self.possible_true_false_values = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']

		# number of test cases to print
		self.num_testcases = int(stdin.readline().strip().split()[0])
		self.values["num_testcases"] = self.num_testcases
		
		# whether to print number of test cases or not i.e self.num_testcases (BOOLEAN)
		self.print_num_testcases = stdin.readline().strip().split()[0]
		self.values["print_num_testcases"] = self.print_num_testcases

		self.options = {}

		# whether the number is float or not (BOOLEAN)
		is_float = stdin.readline().strip().split()[0]
		self.options["is_float"] = is_float

		#minvalue first and then maxvalue with just a space
		minvalue, maxvalue = map(int, raw_input().split())
		self.options["minvalue"] = minvalue
		self.options["maxvalue"] = maxvalue

		self.values["options"] = self.options

		self.__validate_input()

	def __validate_input(self):
		assert self.values['num_testcases'] > 0, "Number of testcases has to be greater than 0"

		assert self.values['print_num_testcases'] in self.possible_true_false_values, "whether to print_num_testcases is not understandable"
		assert self.values['options']['is_float'] in self.possible_true_false_values, "whether numbers to generate is float or not is not understandable"

		assert self.values['options']['minvalue'] < self.values['options']['maxvalue'], "minimum value has to be less than maximum value"

	def get_values(self):
		return self.values

	def print_values(self, values):
		if values['print_num_testcases'] in self.possible_true_false_values[:4]:
			stdout.write(str(values['num_testcases']) + '\n')
		
		if values['options']["is_float"] in self.possible_true_false_values[:4]:
			for i in range(values["num_testcases"]):
				stdout.write(str(random.uniform(values['options']["minvalue"], values['options']["maxvalue"])) + '\n')
		else:
			for i in range(values["num_testcases"]):
				stdout.write(str(random.randint(values['options']["minvalue"], values['options']["maxvalue"])) + '\n')
