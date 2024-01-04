#!/usr/bin/python3
import sys
argc = len(sys.argv)
if argc == 1:
    print("{} arguments.".format(argc - 1), end="\n")
elif argc == 2:
    print("{} argument:".format(argc - 1), end="\n")
else:
    print("{} arguments:".format(argc - 1), end="\n")

i = 1
while argc > 1:
    print(sys.argv[i])
    i += 1
    argc -= 1

