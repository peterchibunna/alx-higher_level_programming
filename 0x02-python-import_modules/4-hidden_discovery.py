#!/usr/bin/python3
if "__main__" == __name__:
    import hidden_4
    for i in dir(hidden_4):
        if not i.startswith("__"):
            print(i)
