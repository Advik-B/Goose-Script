import sys
from termcolor import colored

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

code = boilerplate.replace('<code>', code)

try:
    code = compile(code, '<string>', 'exec')
    eval(code)
except Exception as e:
    tb = sys.exc_info()
    asd = str(tb).split(",")
    try:
        ee = asd[5].replace('"', '').split("\\n")[0]
    except IndexError:
        ee = 'Unknown Location'
    type_ = asd[1].split('(')[0]
    try:
        asda = colored(tb[1].lineno - 3, 'yellow')
    except AttributeError:
        asda = colored('?', 'yellow')
    msg = f"""
Error: {colored(e.args[0], 'red')}
Type of Error: {colored(type_, 'yellow')}
Line: {asda}
Where: {colored(ee, 'cyan')}
    """
    print(msg)
    del tb, asd, ee, type_, msg, asda
    sys.exit(1)