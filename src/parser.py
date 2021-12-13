from functions import *
from keys import *
import sys

if len(sys.argv) == 1:
    print("Usage: ./parser.py <path>")
    sys.exit(1)

file_path = sys.argv[1]

code = []

with open(file_path, 'r') as f:
    for line in f.readlines():
        code.append(line)

#print(*code, sep="\n")

for line in code:
    tmp = line.replace(" ", "")
    if tmp.startswith("#"):
        del tmp
        continue
    if line.startswith('LOG'):
        print(line.split('(')[1].split(')')[0].replace("'", "").replace('"', ''))
        