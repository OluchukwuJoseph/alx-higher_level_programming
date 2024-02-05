#!/usr/bin/python3
"""This module contains a custom list type that inherits the standard List
   1-my_list.py
"""


class MyList(list):
    """This class inherits the standard list
    """
    def print_sorted(self):
        """This method prints the element of an instance in ascending order

            Parameters:
                self: The instance
            Return:
                Nothing
        """
        instance_clone = self.copy()
        for i in range(len(instance_clone)):
            if i < (len(instance_clone) - 1):
                for j in range(len(instance_clone) - 1):
                    if instance_clone[j] > instance_clone[j + 1]:
                        temp = instance_clone[j]
                        instance_clone[j] = instance_clone[j + 1]
                        instance_clone[j + 1] = temp
        print(instance_clone)
