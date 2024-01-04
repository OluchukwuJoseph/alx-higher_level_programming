#!/usr/bin/python3
import calculator_1 as cal
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cal.add(a, b)), end="\n")
    print("{} - {} = {}".format(a, b, cal.sub(a, b)), end="\n")
    print("{} * {} = {}".format(a, b, cal.mul(a, b)), end="\n")
    print("{} / {} = {}".format(a, b, cal.div(a, b)), end="\n")
