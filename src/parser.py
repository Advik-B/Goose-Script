import sys

if len(sys.argv) < 2:
    print("Usage: gooz <path>")
    sys.exit(0)

boilerplate = """
from functions import *
from keys import *
<code>
"""

with open(sys.argv[1], 'r') as f:
    code = f.read()

ad = True
code_ = []
for line in code.splitlines():
    if line.startswith('#'):
        continue
    if line.startswith('#*'):
        ad = False
        continue
    if line.startswith('#*') and not ad:
        ad = True
        continue
    if not ad:
        continue
    code_.append(line)

print(*code_, sep='\n')