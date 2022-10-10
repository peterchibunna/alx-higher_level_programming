#!/usr/bin/python3
def get_length(x):
	total = 0
	if x:
		for i in x:
			total += 1
	return total

def safe_print_list(my_list=[], x=0):
	y = get_length(my_list)
	printable_length = y if x > y else x
	try:
		for i in my_list[:printable_length]:
			print(i, end="")
		print()
		return printable_length
	except Exception:
		pass


def safe_print_integer(value):
	try:
		print("{:d}".format(value))
		return True
	except ValueError:
		return False
