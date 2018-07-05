import random
from sys import stdin, stdout

class RandomNumberGenerator:
	def __init__(self):
		self.values = {}

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

	def get_values(self):
		return self.values

	def print_values(self, values):
		if values['print_num_testcases'] in ['T', 't', 'True', 'true', 'Y', 'y', 'Yes', 'yes']:
			stdout.write(str(values['num_testcases']) + '\n')
		if values['options']["is_float"] in ['T', 't', 'True', 'true', 'Y', 'y', 'Yes', 'yes']:
			stdout.write(str(random.uniform(values['options']["minvalue"], values['options']["maxvalue"])) + '\n')
		else:
			stdout.write(str(random.randint(values['options']["minvalue"], values['options']["maxvalue"])) + '\n')
