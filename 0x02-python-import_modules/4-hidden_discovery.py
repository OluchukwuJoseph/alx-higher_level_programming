#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = sorted(dir(hidden_4))
    for name in names:
        if name[0] == '_':
            continue
        print(name, end="\n")
