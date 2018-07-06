import random
from sys import stdin, stdout

class RandomNumberGenerator:
	def __init__(self):
		self.values = {}
		self.options = {}
		self.values["options"] = self.options

		self.possible_true_false_values = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']

		# number of test cases to print
		self.num_testcases = int(stdin.readline().strip().split()[0])
		self.store_num_testcases(self.num_testcases)
		
		# whether to print number of test cases or not i.e self.num_testcases (BOOLEAN)
		self.print_num_testcases = stdin.readline().strip().split()[0]
		self.store_print_num_testcases(self.print_num_testcases)

		# whether the number is float or not (BOOLEAN)
		is_float = stdin.readline().strip().split()[0]
		self.store_is_float(is_float)

		#minvalue first and then maxvalue with just a space
		minvalue, maxvalue = map(int, raw_input().split())
		self.store_minvalue_and_maxvalue([minvalue, maxvalue])

	def store_num_testcases(self, num_testcases):
		if type(num_testcases) != int:
			raise TypeError("number of test cases needs to be an integer.")
		else:
			if num_testcases <= 0:
				raise ValueError("number of test cases needs to be positive.")
			else:
				self.values['num_testcases'] = num_testcases

	def store_print_num_testcases(self, print_num_testcases):
		if print_num_testcases in self.possible_true_false_values:
			self.values['print_num_testcases'] = print_num_testcases
		else:
			raise ValueError("whether to print test cases or not is invalid.")

	def store_is_float(self, is_float):
		if is_float in self.possible_true_false_values:
			self.values['options']['is_float'] = is_float
		else:
			raise ValueError("whehter to have float numbers or not is invalid.")

	def store_minvalue_and_maxvalue(self, min_and_max_values):
		minvalue = min_and_max_values[0]
		maxvalue = min_and_max_values[1]

		if type(minvalue) != int or type(maxvalue) != int:
			raise TypeError("type of maximum value and mininum value needs to be int.")
		else:
			if maxvalue - minvalue <= 0:
				raise ValueError("mininum value must be less than maximum value")
			else:
				self.values['options']['minvalue'] = minvalue
				self.values['options']['maxvalue'] = maxvalue

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
