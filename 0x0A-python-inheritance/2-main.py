#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class
MyList = __import__('1-my_list').MyList
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

my_list = MyList()
if is_same_class(my_list, list):
    print("{} is an instance of the class {}".format(my_list, list.__name__))
