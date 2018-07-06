import random
from sys import stdin, stdout
import string
import copy


class RandomStringGenerator:
	def __init__(self):
		self.values = {}
		self.possible_true_false_values = ['T', 't', 'Y', 'y', 'F', 'f', 'N', 'n']

		# number of test cases
		self.num_testcases = int(stdin.readline().strip().split()[0])
		self.values['num_testcases'] = self.num_testcases

		# whether to print number of test cases or not
		self.print_num_testcases = stdin.readline().strip().split()[0]
		self.values['print_num_testcases'] = self.print_num_testcases

		self.options = {}

		# size of string
		self.string_size = int(stdin.readline().strip().split()[0])
		self.options['string_size'] = self.string_size

		# whether to print size of string or not
		self.print_string_size = stdin.readline().strip().split()[0]
		self.options['print_string_size'] = self.print_string_size

		# whether string should contain distinct numbers or not
		self.distinct = stdin.readline().strip().split()[0]
		self.options['distinct'] = self.distinct

		# whether uppercase, lowercase, digits, punctuation are allowed or not resp.
		self.allowed = stdin.readline().strip().split()[0]
		self.options['allowed'] = self.allowed

		self.values['options'] = self.options

		self.possible_letters = ''
		for i in range(4):
			if i == 0 and self.values['options']['allowed'][0] in self.possible_true_false_values[:4]:
				self.possible_letters += string.uppercase
			elif i == 1 and self.values['options']['allowed'][1] in self.possible_true_false_values[:4]:
				self.possible_letters += string.lowercase
			elif i == 2 and self.values['options']['allowed'][2] in self.possible_true_false_values[:4]:
				self.possible_letters += string.digits
			elif i == 3 and self.values['options']['allowed'][3] in self.possible_true_false_values[:4]:
				self.possible_letters += string.punctuation

		self.__validate_values()

	def get_values(self):
		return self.values

	def __validate_values(self):
		assert self.values['num_testcases'] > 0, "Number of test cases provided has to be greater than 0"
		assert self.values['print_num_testcases'] in self.possible_true_false_values, "whether to print number of test cases or not is not understandable"

		assert self.values['options']['string_size'] > 0, "Invalid requested size of string"
		assert self.values['options']['print_string_size'] in self.possible_true_false_values, "Invalid choice for whether printing string size or not"

		assert self.values['options']['distinct'] in self.possible_true_false_values, "Invalid distinct or not value"

		assert len(self.possible_letters) > 0, "Carefully enter the choice of allowed letters"
		
		assert len(self.values['options']['allowed']) == 4, "Carefully enter the 4 valid letters for the choice of letters"
		for y_n in self.values['options']['allowed']:
			assert y_n in self.possible_true_false_values, "allowed values cannot be identified correctly"

	def print_values(self, values):
		if values['print_num_testcases'] in self.possible_true_false_values[:4]:
			stdout.write(str(values['num_testcases']) + '\n')

		for _ in range(values['num_testcases']):
			if values['options']['print_string_size'] in self.possible_true_false_values[:4]:
				stdout.write(str(values['options']['string_size']) + '\n')

			ans = ''
			if values['options']['distinct'] in self.possible_true_false_values[:4]:
				if values['options']['string_size'] > len(self.possible_letters):
					raise ValueError("Required amount of distinct letters cannot be created in the chosen range")
				
				temp_possible_letters = list(self.possible_letters)
				j = 0
				while j != values['options']['string_size']:
					random_letter = temp_possible_letters.pop(random.randint(0, len(temp_possible_letters)-1))
					ans += random_letter
					j += 1
				ans = ''.join(ans)
			else:
				ans = ''.join(random.choice(self.possible_letters) for i in range(values['options']['string_size']))

			stdout.write(str(ans) + '\n')