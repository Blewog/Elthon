# INSTALLATION
### (These installation processes were tested in github codespaces (also only for bash cause thats what VSCode uses (so basically if you have windows and dont have VSCode figure it out)))
The installation is quite simple and the reason i chose this way is because i was looking for a solution that works with github codepaces and this one does. (also i probably messed up somewhere in the packaging)
```
git clone https://github.com/Blewog/Elthon
cd Elthon
pip install -e .
```
Or if you want to install a certain version here are the commands to do so, (ill be using the first version as an example)
```
curl -L https://github.com/Blewog/Elthon/archive/refs/tags/v0.0.1-Alpha.zip --output Elthon.zip
unzip Elthon.zip
cd Elthon-0.0.1-Alpha
pip install -e .
```
then once you get back to your project path type:
```
mv Elthon-0.0.1-Alpha Elthon_0_0_1_Alpha
```
the mv command is to rename it because it cant import ones with "-" and "." and stuff.
for it to work you must change it from
```
import Elthon.Elthon
```
to
```
import Elthon_0_0_1_Alpha
```
or whatever the folder is named.

# DOCUMENTATION (W.I.P. (Both this and the library))
## The write function
### write.console()
write.console() is essentially just print. example: write.console("Hello World!") which would print "Hello, World!". Heres a breakdown of the function: its just print so the thing in quotations is what will be printed.\
Heres a basic example and its output.
```
from Elthon.Elthon import write

write.console("Hello, World")
```
Output: Hello, World!

### write.undrline()
write.undrline() is near the same as write.console(), ill show you an example: write.undrline("Hello, World!") which would print "<ins>Hello, World!</ins>" thats all you need to know since its near the same as write.console() but it underlines.\
Heres a basic example and its output
```
from Elthon.Elthon import write

write.undrline("Hello, World!")
```
Output: <ins>Hello, World!</ins>

### write.bold()
write.bold() is also near the same as write.console(), heres an example: write.bold("Hello, World!") which would print "__Hello, World!__" just the same as the others but it bolds.\
Heres a basic example and its output:
```
from Elthon.Elthon import write

write.bold("Hello, World")
```
Output: __Hello, World!__

### extras
This explanation wont be too long. there are currently three things you can change which are color and the end and you can print out the save history, the available colors are purple, cyan, darkcyan, blue, green, yellow, and red. And the end one is just end on print.\
Heres an example of the History one (assuming it was clear before):
```
from Elthon.ELthon import write, save

save.text("Hello")
write.console("", History=True)
```
Output: Hello

## The message function
### message.info()
message.info() prints an info message box. Example: message.info("Hello, World!") (i cant show what it would prints here because it doesnt really let me)\
Heres a basic example:
```
from Elthon.Elthon import message

message.info("Hello, World!")
```
Output: N/A

### message.warn()
message.warn() prints a warning message box. Example: message.info("Hello, World!")\
Heres a basic example:
```
from Elthon.Elthon import message

message.warn("Hello, World!")
```
Output: N/A

### message.err()
message.err() prints an error message box. Example: message.err("Hello, World!")\
Heres a basic example:
```
from Elthon.Elthon import message

message.err("Hello, World!")
```
Output: N/A

## The save function
### save.text()
save.text() saves text to the SaveFunctionHistory.txt file (or whatever file you put in the paranthesis) sort of like a clipboard.\
Heres a basic example:
```
from Elthon.Elthon import save

save.text("Hello, World")
```
Output: N/A (No output it just saves.)

### save.history()
save.history() returns the history of the txt file.\
Heres a basic example:
```
from Elthon.Elthon import save

history = save.history()
```
Output N/A (it put the history into the history variable)

### save.clear()
save.clear() clears the text in SaveFunctionHistory.txt (or whatever file you put in the paranthesis.)\
Heres a basic example:
```
from Elthon.Elthon import save

save.clear()
```
Output: N/A (it cleared the history)
