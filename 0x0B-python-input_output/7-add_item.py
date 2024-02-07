#!/usr/bin/python3
"""This python script adds all arguments to a Python list,
   and then save them to a JSON file
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

command_line_arguments = []
arguments = []

for arg in sys.argv:
    if arg is not sys.argv[0]:
        command_line_arguments.append(arg)

try:
    my_list = load_from_json_file(filename)

except (FileNotFoundError, FileExistsError):
    my_list = []

finally:
    arguments = command_line_arguments + my_list
    save_to_json_file(arguments, filename)
