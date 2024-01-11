#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = {}
    dictionary.update(a_dictionary)
    for key in dictionary.keys():
        dictionary.update({key: (dictionary.get(key) * 2)})
    return dictionary
