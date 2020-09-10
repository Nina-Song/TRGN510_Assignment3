#!/usr/bin/python
import sys
import fileinput
import re

phone_num_file = sys.argv[1]
lookup_code = {}
for each_line in fileinput.input(phone_num_file):
    area_code = re.sub(r'\D', '', each_line)
    area_code = area_code[0:3]
    print(area_code)

