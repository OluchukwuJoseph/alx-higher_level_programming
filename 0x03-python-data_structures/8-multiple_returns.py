#!/usr/bin/python3
def multiple_returns(sentence):
    try:
        new_tuple = (len(sentence), sentence[0])
    except IndexError:
        new_tuple = (len(sentence), None)
    return new_tuple
