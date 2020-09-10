#!/usr/bin/python
import sys
import fileinput
import re
import json

my_gene_file = sys.argv[1]
dataset = []
Homo_sapiens = {}
for each_line_of_text in fileinput.input(my_gene_file):
    if each_line_of_text.startswith("#"):
        continue
    splitcolumn_array = re.split(r'[;,\t,\"]',each_line_of_text)
    chro =splitcolumn_array[0]
    startPos = (int)(splitcolumn_array[3])
    endPos =(int)(splitcolumn_array[4])
    id_geneName = splitcolumn_array.index(' gene_name ') + 1
    geneName = splitcolumn_array[id_geneName]
    
    Homo_sapiens = {"geneName":geneName, "chr":chro, "startPos":startPos, "endPos":endPos}
    dataset.append(Homo_sapiens)

j = json.dumps(dataset, indent=1)
print(j)
