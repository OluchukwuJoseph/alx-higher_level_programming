#!/usr/bin/python3
for i in range(100):
    if (i // 10) == (i % 10):
        continue
    for x in range(1, i):
        if (i % 10) == (x // 10):
            break
    else:
        if i != 89:
            print("{:02}".format(i), end=", ")
        else:
            print("{:02}".format(i), end="\n")
