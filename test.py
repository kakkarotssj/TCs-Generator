from strings import RandomStringGenerator
from numbers import RandomNumberGenerator
from arrays import RandomArrayGenerator


class Generators:
	def __init__(self):
		pass

	def generate_numbers(self):
		rng = RandomNumberGenerator()
		values = rng.get_values()
		rng.print_values(values)

	def generate_arrays(self):
		rag = RandomArrayGenerator()
		values = rag.get_values()
		rag.print_values(values)

	def generate_strings(self):
		rsg = RandomStringGenerator()
		values = rsg.get_values()
		rsg.print_values(values)

generator = Generators()
# generator.generate_numbers()
# generator.generate_arrays()
generator.generate_strings()
