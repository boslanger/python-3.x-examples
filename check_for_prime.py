"""
With a given range, the program will return all the primary numbers.
Python 3.6.4
9 NOV 2018
Focus on try/except/else block to catch invalid user input.
"""
import math


def is_prime(n):
	"""check for prime; returns true if prime."""
	try:
		n = int(n) # Verifies the user supplied an integer
	except ValueError:
		print("You must give an integer.") # Feedback to user
	else:
		if n == 1:
			return False # 1 is not prime
		if n == 2:
			return True
		if n > 2 and n % 2 == 0: # 2 and its multiples are not prime
			return False

		max_divisor = math.floor(math.sqrt(n))
		for d in range(3, 1 + max_divisor, 2):
			"""range 3 to 1 plus the max divisor in increments of two."""
			# Called in attempt to speed compilation
			if n % d == 0:
				return False
		return True


# checks for functionality
for i in range(5):
	number = input("Which number would you like to check for prime?")
	print(number, is_prime(number))

# checks for range output
for n in range (1, 100):
	print(n, is_prime(n))

