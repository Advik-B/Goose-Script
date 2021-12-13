from functions import *
from keys import *
import sys
import functions

if len(sys.argv) == 1:
    print("Usage: ./parser.py <path>")
    sys.exit(1)

file_path = sys.argv[1]

code = []

with open(file_path, 'r') as f:
    for line in f.readlines():
        code.append(line)

#print(*code, sep="\n")

code_ = []

for line in code:
    tmp = line.replace(" ", "")
    if tmp.startswith("#"):
        del tmp
        continue
    line_ = []
    for letter in line:
        if letter == ' ':
            letter = ''
        line_.append(letter)
    code_.append(line_)

del line_
code = code_
del code_

print(*code, sep="\n")