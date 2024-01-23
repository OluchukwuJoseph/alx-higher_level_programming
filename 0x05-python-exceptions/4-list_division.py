#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            new_list += [my_list_1[i] / my_list_2[i], ]
        except Exception as error:
            if isinstance(error, ZeroDivisionError):
                new_list += [0, ]
                print("division by 0")
                continue
            elif isinstance(error, TypeError):
                new_list += [0, ]
                print("wrong type")
            elif isinstance(error, IndexError):
                print("out of range")
                for i in range(list_length - len(new_list)):
                    new_list += [0, ]
                break
    return new_list
