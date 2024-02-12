#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

    print('---')
    r3 = Rectangle(3, 2, 0, 3)
    r3.display()

    print('---')
    r4 = Rectangle(2, 3, 3, 4)
    r4.display()
