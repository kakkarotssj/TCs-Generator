import random
from sys import stdin, stdout

class RandomArrayGenerator:
	def __init__(self):
		self.values = {}
		self.possible_true_false_values = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']

		# number of test cases
		self.num_testcases = int(stdin.readline().strip().split()[0])
		self.values["num_testcases"] = self.num_testcases

		# whether to print number of test cases i.e num_testcases (BOOLEAN)
		self.print_num_testcases = stdin.readline().strip().split()[0]
		self.values["print_num_testcases"] = self.print_num_testcases

		self.options = {}
		# size of array
		self.array_size = int(stdin.readline().strip().split()[0])
		self.options["array_size"] = self.array_size

		# whether to print size of array or not (BOOLEAN)
		self.print_array_size = stdin.readline().strip().split()[0]
		self.options["print_array_size"] = self.print_array_size

		# whether numbers in the array are in increasing order
		self.strictly_increasing = stdin.readline().strip().split()[0]
		self.options["strictly_increasing"] = self.strictly_increasing

		# whether numbers in the array has to be distinct or not (BOOLEAN)
		self.distinct = stdin.readline().strip().split()[0]
		self.options["distinct"] = self.distinct

		# minvalue and maxvalue in the array 
		self.minvalue, self.maxvalue = map(int, stdin.readline().strip().split())
		self.options["minvalue"] = self.minvalue
		self.options["maxvalue"] = self.maxvalue

		self.values["options"] = self.options

		self.__validate_input()

	def get_values(self):
		return self.values

	def __validate_input(self):
		assert self.values['num_testcases'] > 0, "Number of test cases provided has to be greater than 0"
		assert self.values['print_num_testcases'] in self.possible_true_false_values, "whether to print number of test cases or not is not understandable"

		assert self.values['options']['array_size'] > 0, "Size of array has to be greater than 0"
		assert self.values['options']['print_array_size'] in self.possible_true_false_values, "whether to print size of array or not is not understandable"

		assert self.values['options']['distinct'] in self.possible_true_false_values, "whether elements in array are distinct or not is not understandable"
		assert self.values['options']['strictly_increasing'] in self.possible_true_false_values, "whether elements in array are strictly increasing or not is not understandable"

		assert self.values['options']['minvalue'] < self.values['options']['maxvalue'], "min value for array elements has to be less than max value"

		if self.values['options']['distinct'] in self.possible_true_false_values[:4] or self.values['options']['strictly_increasing'] in self.possible_true_false_values[:4]:
			assert self.values['options']['array_size'] < self.values['options']['maxvalue'] - self.values['options']['minvalue'] + 1

	def _get_distinct_values(self, values, arr):
		partitions = [[values['options']['minvalue'], values['options']['maxvalue']]]
		length_partitions = 1

		j = 0
		while j != values['options']['array_size']:
			random_index = random.randint(0, length_partitions-1)
			partition_number = random.randint(partitions[random_index][0], partitions[random_index][1])
			arr.append(partition_number)
			
			if partition_number-1 >= partitions[random_index][0]:
				partitions.insert(random_index+1, [partitions[random_index][0], partition_number-1])
				length_partitions += 1
			
			if partition_number+1 <= partitions[random_index][1]:
				partitions.insert(random_index+2, [partition_number+1, partitions[random_index][1]])
				length_partitions += 1
			
			partitions.pop(random_index)
			length_partitions -= 1

			j += 1

		return arr

	def print_values(self, values):
		if values["print_num_testcases"] in self.possible_true_false_values[:4]:
			stdout.write(str(values["num_testcases"]) + '\n')
		
		print_array_size = False
		if values['options']['print_array_size'] in self.possible_true_false_values[:4]:
			print_array_size = True

		distinct = False
		if values['options']['distinct'] in self.possible_true_false_values[:4]:
			distinct = True

		strictly_increasing = False
		if values['options']['strictly_increasing'] in self.possible_true_false_values[:4]:
			distinct = True

		for i in range(values["num_testcases"]):
			if print_array_size:
				stdout.write(str(values["options"]["array_size"]) + '\n')

			arr = []

			# below are the three possible values of distinct and strictly_increasing values
			# 1) distinct --> False and strictly_increasing --> False
			if not distinct and not strictly_increasing:
				for j in range(values['options']["array_size"]):
					arr.append(random.randint(values["options"]["minvalue"], values["options"]["maxvalue"]))

			# 2) strictly_increasing --> True
			if strictly_increasing:
				step = float(values["options"]["maxvalue"] - values["options"]["minvalue"] + 1) / float(values["options"]["array_size"])
				if 1.0 < step < 2.0:
					if values['options']['array_size'] == 1:
						arr.append(values['options']['minvalue'])
					else:
						arr = self._get_distinct_values(values, arr)
						arr.sort()
				else:
					step = int(step)

					partition_minvalue = values['options']['minvalue']
					j = 0
					while j != values['options']['array_size']:
						arr.append(random.randint(partition_minvalue, partition_minvalue+step-1))
						partition_minvalue += step

						j += 1

			# 3) distinct --> True and strictly_increasing --> False
			if distinct and not strictly_increasing:
				arr = self._get_distinct_values(values, arr)

			# 4) distinct --> True and strictly_increasing --> True would just be same as case 2
			# no need to write code again

			stdout.write(' '.join(str(element) for element in arr) + '\n')