import sys
import functions
import keys

if len(sys.argv) == 1:
    print("Usage: ./parser.py <path>")
    sys.exit(1)

file_path = sys.argv[1]

code = []

with open(file_path, 'r') as f:
    for line in f.readlines():
        code.append(line)
