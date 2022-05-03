import csv
import numbers
from tokenize import Number

dict_from_csv = {}

with open('muska_imena.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: int(rows[1]) for rows in reader}

print(dict_from_csv)
