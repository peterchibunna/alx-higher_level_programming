#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	y = sum(1 for c in my_list) if my_list else 0
	printable_length = y if x > y else x
	try:
		for i in my_list[:printable_length]:
			print(i, end="")
		print()
		return printable_length
	except Exception:
		pass

