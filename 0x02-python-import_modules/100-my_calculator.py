#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]), end="\n")
        sys.exit(1)

    operator = sys.argv[2]
    if operator == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result), end="\n")
    elif operator == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], result), end="\n")
    elif operator == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], result), end="\n")
    elif operator == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], result), end="\n")
    else:
        print("Unknown operator. Available operators: +, -, * and /", end="\n")
        sys.exit(1)
