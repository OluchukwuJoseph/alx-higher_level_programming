#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    result = 0
    for key in a_dictionary.keys():
        if a_dictionary.get(key) > result:
            result = a_dictionary.get(key)
            max_key = ''
            max_key += key
    return max_key
