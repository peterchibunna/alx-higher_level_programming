#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError): # shall skip IndexError
            continue
        else:
            total += 1
    print("")
    return total
