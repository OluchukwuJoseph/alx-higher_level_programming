#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
my_list2 = MyList()
my_list2.append("Joseph")
my_list2.append("Oluchukwu")
my_list2.append("Other names")
my_list2.print_sorted()
my_list3 = MyList()
my_list3.print_sorted()
