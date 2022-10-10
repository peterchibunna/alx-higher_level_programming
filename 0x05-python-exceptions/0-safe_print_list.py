#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	y = my_list.__len__()
	printable_length = y if x > y else x
	try:
		for i in my_list[:printable_length]:
			print(i, end="")
		print()
		return printable_length
	except Exception:
		pass

