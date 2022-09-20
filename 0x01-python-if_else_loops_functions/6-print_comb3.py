#!/usr/bin/python3
print(", ".join(["{}{}".format(x, y)
                 for x in range(0, 10)
                 for y in range(0, 10) if x != y and x < y]))
