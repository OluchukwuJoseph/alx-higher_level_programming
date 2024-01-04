#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    i = 1
    argc = len(sys.argv)
    while argc > 1:
        argument = sys.argv[i]
        sum += int(argument)
        i += 1
        argc -= 1
    print(sum)
