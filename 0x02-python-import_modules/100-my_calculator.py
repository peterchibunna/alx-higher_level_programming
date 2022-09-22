#!/usr/bin/python3
if "__main__" == __name__:
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        if op not in ['+', '-', '*', '/']:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if op == '+':
                print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            elif op == '-':
                print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            elif op == '*':
                print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            elif op == '/':
                print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            exit(0)
