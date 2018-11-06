"""
jbollinger@yahoo.com
6 NOV 2018
Change Maker
Code that outputs amount of bills and coins.
"""


def count_change(change):
	"""A Function to calculate the change."""
	# This block of local variables to hold the change.
	hundred = 0
	twenty = 0
	ten = 0
	five = 0
	single = 0
	if type(change) == str:
		print("You must use only integers or floats.")
	if type(change) != str:

		while change >= 1:
			"""main loop that increments the change counters."""
			if change >= 100:
				change = change - 100
				hundred += 1
				continue #has to be called to start the while loop over.
			if change >= 20:
				change = change - 20
				twenty += 1
			if change >= 10:
				change = change - 10
				ten += 1
			if change >= 5:
				change = change - 5
				five += 1
			if change >= 1:
				change = change - 1
				single += 1

		# print("this should be zero or change: ", change) # for testing
		"""This is for counting out the bills."""
		if hundred > 0:
			print("Hundreds:", hundred)
		if twenty > 0:
			print("Twenties:", twenty)
		if ten > 0:
			print("Tens:", ten)
		if five > 0:
			print("Fives:", five)
		if single > 0:
			print("Dollars:", single)

		"""This is for coin change only."""
		change = round(change, 2) * 100
		if change >= 25:
			print("Quarters:", int(change//25))
		change = change%25
		if change >= 10:
			print("Dimes:", int(change//10))
		change = change%10
		if change >= 5:
			print("Nickles:", int(change//5))
		change = change%5
		if change > 0:
			print("Pennies:", int(change//1))



"""These simply check for functionality."""

total = 342.59
amount_paid = 500
difference = amount_paid - total
difference = round(difference, 2)

print("\niteration 1 'var'")
count_change(difference) # good
print("\niteration 2 'int(410):")
count_change(401) # good
print("\niteration 3 'str(asdf)'")
count_change('asdf') # good
print("\niteration 4 'float(410.02)'")
count_change(483.42) # good
print("\niteration 5 'Nonsense'")
x = input("nonsense") # good
count_change(x)

