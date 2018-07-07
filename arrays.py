import random
from sys import stdin, stdout

class RandomArrayGenerator:
	def __init__(self):
		self.values = {}
		self.options = {}
		self.values["options"] = self.options

		self.possible_true_false_values = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']

		# number of test cases
		self.num_testcases = int(stdin.readline().strip().split()[0])
		self.store_num_testcases(self.num_testcases)

		# whether to print number of test cases i.e num_testcases (BOOLEAN)
		self.print_num_testcases = stdin.readline().strip().split()[0]
		self.store_print_num_testcases(self.print_num_testcases)

		self.options = {}
		# size of array
		self.array_size = int(stdin.readline().strip().split()[0])
		self.store_array_size(self.array_size)

		# whether to print size of array or not (BOOLEAN)
		self.print_array_size = stdin.readline().strip().split()[0]
		self.store_print_array_size(self.print_array_size)

		# whether numbers in the array are in increasing order
		self.strictly_increasing = stdin.readline().strip().split()[0]
		self.store_strictly_increasing(self.strictly_increasing)

		# whether numbers in the array has to be distinct or not (BOOLEAN)
		self.distinct = stdin.readline().strip().split()[0]
		self.store_distinct(self.distinct)

		# minvalue and maxvalue in the array 
		self.minvalue, self.maxvalue = map(int, stdin.readline().strip().split())
		self.store_minvalue_and_maxvalue([[self.minvalue, self.maxvalue], self.values])

	def store_num_testcases(self, num_testcases):
		if type(num_testcases) != int:
			raise TypeError("number of test cases needs to be an integer.")
		else:
			if num_testcases <= 0:
				raise ValueError("number of test cases needs to be positive.")
			else:
				self.values['num_testcases'] = num_testcases

	def store_print_num_testcases(self, print_num_testcases):
		if type(print_num_testcases) != str:
			raise TypeError("whether to print num testcases or not should be string only")
		else:
			if print_num_testcases in self.possible_true_false_values:
				self.values['print_num_testcases'] = print_num_testcases
			else:
				raise ValueError("whether to print test cases or not is invalid.")

	def store_array_size(self, array_size):
		if type(array_size) != int:
			raise TypeError("array size needs to be an integer.")
		else:
			if array_size <= 0:
				raise ValueError("array size needs to be positive.")
			else:
				self.values['options']['array_size'] = array_size

	def store_print_array_size(self, print_array_size):
		if type(print_array_size) != str:
			raise TypeError("whether to print array size or not should be string only")
		else:
			if print_array_size in self.possible_true_false_values:
				self.values['options']['print_array_size'] = print_array_size
			else:
				raise ValueError("whether to print array size or not is invalid.")

	def store_strictly_increasing(self, strictly_increasing):
		if type(strictly_increasing) != str:
			raise TypeError("whether to have strictly_increasing integers in array or not should be string only")
		else:
			if strictly_increasing in self.possible_true_false_values:
				self.values['options']['strictly_increasing'] = strictly_increasing
			else:
				raise ValueError("whether to have strictly_increasing integers in array or not or not is invalid.")

	def store_distinct(self, distinct):
		if type(distinct) != str:
			raise TypeError("whether to have distinct integers in array or not should be string only")
		else:
			if distinct in self.possible_true_false_values:
				self.values['options']['distinct'] = distinct
			else:
				raise ValueError("whether to have distinct integers in array or not or not is invalid.")

	def store_minvalue_and_maxvalue(self, params):
		min_and_max_values = params[0]
		minvalue = min_and_max_values[0]
		maxvalue = min_and_max_values[1]

		strictly_increasing, distinct = params[1]['options']['strictly_increasing'], params[1]['options']['distinct']
		array_size = params[1]['options']['array_size']

		if type(minvalue) != int or type(maxvalue) != int:
			raise TypeError("type of maximum value and mininum value needs to be int.")
		else:
			if maxvalue - minvalue <= 0:
				raise ValueError("mininum value must be less than maximum value")
			else:
				if strictly_increasing in self.possible_true_false_values[:4] or distinct in self.possible_true_false_values[:4]:
					if array_size > maxvalue - minvalue + 1:
						raise ValueError("sufficient number of integers cannot be created. Please check options again.")
			self.values['options']['minvalue'] = minvalue
			self.values['options']['maxvalue'] = maxvalue

	def get_values(self):
		return self.values

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
			strictly_increasing = True

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