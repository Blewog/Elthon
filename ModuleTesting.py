# This is just for me to test the module.

import sys
from Elthon import write, save, message

write.console("Hello")
response = sys.stdin.readline()
save.text(response)
save.history()
write.console("", history=True)
