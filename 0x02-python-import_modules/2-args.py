#!/usr/bin/python3
if "__main__" == __name__:
    import sys
    length = len(sys.argv) - 1
    print("{} argument{}{}".format(length, ""
          if length == 1 else "s", "." if length == 0 else ":"))
    for idx, i in enumerate(list(range(0, length + 1))):
        if idx == 0:
            continue
        print("{}: {}".format(idx, sys.argv[i]))
