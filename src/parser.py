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

code2 = []
for line in code:
    raw = line.replace(' ', '').replace('	', '')
    if raw.startswith('#') and not raw.startswith('#*'):
        continue
    if raw.startswith('\n'):
        continue

    code2.append(line)

code.clear()
code.extend(code2)
code2.clear()

print(*code, sep='\n')