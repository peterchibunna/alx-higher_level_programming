#!/usr/bin/python3
if "__main__" == __name__:
    import sys
    sum = 0
    for idx, i in enumerate(sys.argv):
        if idx == 0:
            continue
        sum += int(i)
    print(sum)
