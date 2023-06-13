#!/usr/bin/python3
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
json_list = []

if os.path.exists(file_name):
    json_list = load_from_json_file(file_name)

for i in sys.argv[1:]:
    json_list.append(i)

save_to_json_file(json_list, file_name)
