#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = (sys.argv[2])
    if operator == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
