import random
from sys import stdin, stdout
import string
import copy


class RandomStringGenerator:
	def __init__(self):
		self.values = {}
		self.options = {}
		self.values['options'] = self.options

		self.possible_true_false_values = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']

		# number of test cases
		self.num_testcases = int(stdin.readline().strip().split()[0])
		self.store_num_testcases(self.num_testcases)

		# whether to print number of test cases or not
		self.print_num_testcases = stdin.readline().strip().split()[0]
		self.store_print_num_testcases(self.print_num_testcases)

		# size of string
		self.string_size = int(stdin.readline().strip().split()[0])
		self.store_string_size(self.string_size)

		# whether to print size of string or not
		self.print_string_size = stdin.readline().strip().split()[0]
		self.store_print_string_size(self.print_string_size)

		# whether string should contain distinct numbers or not
		self.distinct = stdin.readline().strip().split()[0]
		self.store_distinct(self.distinct)

		# whether uppercase, lowercase, digits, punctuation are allowed or not resp.
		self.allowed = stdin.readline().strip().split()[0]
		self.store_allowed(self.allowed)

		self.store_possible_letters(self.allowed)

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

	def store_string_size(self, string_size):
		if type(string_size) != int:
			raise TypeError("string_size needs to be an integer.")
		else:
			if string_size <= 0:
				raise ValueError("string_size needs to be positive.")
			else:
				self.values['options']['string_size'] = string_size

	def store_print_string_size(self, print_string_size):
		if type(print_string_size) != str:
			raise TypeError("whether to print string size or not should be string only")
		else:
			if print_string_size in self.possible_true_false_values:
				self.values['options']['print_string_size'] = print_string_size
			else:
				raise ValueError("whether to print string size or not is invalid.")

	def store_distinct(self, distinct):
		if type(distinct) != str:
			raise TypeError("whether to have distinct characters choice should be string only")
		else:
			if distinct in self.possible_true_false_values:
				self.values['options']['distinct'] = distinct
			else:
				raise ValueError("whether to have distinct letters or not is invalid.")

	def store_allowed(self, allowed):
		if type(allowed) != str:
			raise TypeError("Allowed characters choice must be string only.")
		else:
			if len(allowed) != 4:
				raise ValueError("choice of allowed characters must be 4 lenghts only.")
			else:
				set_allowed = list(set(allowed))
				if len(set_allowed) == 1 and set_allowed == ['n']:
					raise ValueError("Atleast one type of letter must be allowed.")
				else:
					for char in allowed:
						if char not in self.possible_true_false_values:
							raise ValueError("choice for allowed characters is not understandable")

		self.values['options']['allowed'] = allowed

	def store_possible_letters(self, allowed):
		possible_letters = ''
		for i in range(4):
			if i == 0 and allowed[0] in self.possible_true_false_values[:4]:
				possible_letters += string.uppercase
			elif i == 1 and allowed[1] in self.possible_true_false_values[:4]:
				possible_letters += string.lowercase
			elif i == 2 and allowed[2] in self.possible_true_false_values[:4]:
				possible_letters += string.digits
			elif i == 3 and allowed[3] in self.possible_true_false_values[:4]:
				possible_letters += string.punctuation

		if len(possible_letters) < self.values['options']['string_size']:
			raise ValueError("Required amount of distinct letters cannot be created in the chosen range")

		self.values['possible_letters'] = possible_letters

	def get_values(self):
		return self.values

	def print_values(self, values):
		if values['print_num_testcases'] in self.possible_true_false_values[:4]:
			stdout.write(str(values['num_testcases']) + '\n')

		print_string_size = False
		if values['options']['print_string_size'] in self.possible_true_false_values[:4]:
			print_string_size = True

		distinct = False
		if values['options']['distinct'] in self.possible_true_false_values[:4]:
			distinct = True

		for _ in range(values['num_testcases']):
			if print_string_size:
				stdout.write(str(values['options']['string_size']) + '\n')

			if distinct:
				ans = get_distinct_letters(values['possible_letters'], values['options']['string_size'])
			else:
				ans = get_random_letters(values['possible_letters'], values['options']['string_size'])

			stdout.write(str(ans) + '\n')

def get_distinct_letters(possible_letters, string_size):
	temp_possible_letters = list(possible_letters)
	j = 0
	ans = ''
	while j != string_size:
		random_letter = temp_possible_letters.pop(random.randint(0, len(temp_possible_letters) - 1))
		ans += random_letter
		j += 1
	
	return ans

def get_random_letters(possible_letters, string_size):
	ans = ''.join(random.choice(possible_letters) for i in range(string_size))

	return ans