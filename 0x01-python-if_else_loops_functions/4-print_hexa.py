#!/usr/bin/python3
print("".join(["{} = {}\n".format(a, hex(a)) for a in range(0, 98+1)]), end="")
