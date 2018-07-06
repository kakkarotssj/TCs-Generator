import random
from sys import stdin, stdout
import string
import copy


class RandomStringGenerator:
	def __init__(self):
		self.values = {}

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

	def get_values(self):
		return self.values

	def print_values(self, values):
		if values['print_num_testcases'] in ['T', 't', 'y', 'Y']:
			stdout.write(str(values['num_testcases']) + '\n')

		possible_letters = ''
		for i in range(4):
			if i == 0 and values['options']['allowed'][0] in ['T', 't', 'y', 'Y']:
				possible_letters += string.uppercase
			elif i == 1 and values['options']['allowed'][1] in ['T', 't', 'y', 'Y']:
				possible_letters += string.lowercase
			elif i == 2 and values['options']['allowed'][2] in ['T', 't', 'y', 'Y']:
				possible_letters += string.digits
			elif i == 3 and values['options']['allowed'][3] in ['T', 't', 'y', 'Y']:
				possible_letters += string.punctuation

		if len(possible_letters) <= 0:
			raise ValueError("Carefully enter the values you want in string")

		if len(values['options']['allowed']) != 4:
			raise ValueError("Carefully enter the choice of allowed letters")

		for _ in range(values['num_testcases']):
			if values['options']['print_string_size'] in ['T', 't', 'y', 'Y']:
				stdout.write(str(values['options']['string_size']) + '\n')

			ans = ''
			if values['options']['distinct'] in ['T', 't', 'y', 'Y']:
				if values['options']['string_size'] > len(possible_letters):
					raise ValueError("Required amount of distinct letters cannot be created in the chosen range")
				
				temp_possible_letters = list(possible_letters)
				j = 0
				while j != values['options']['string_size']:
					random_letter = temp_possible_letters.pop(random.randint(0, len(temp_possible_letters)-1))
					ans += random_letter
					j += 1
				ans = ''.join(ans)
			else:
				ans = ''.join(random.choice(possible_letters) for i in range(values['options']['string_size']))

			stdout.write(str(ans) + '\n')