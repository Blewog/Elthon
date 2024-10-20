# INSTALLATION
The installation i quite simple and the reason i chose this way is because i was looking for a solution that works with github codepaces. 
```
git clone https://github.com/Blewog/Elthon
cd Elthon
pip install -e .
```

# DOCUMENTATION (Please keep in mind this is a work in progress)
## The write function
### write.console()
write.console() is essentially just print. example: write.console("Hello World!") which would print "Hello, World!". Heres a breakdown of the function: its just print so the thing in quotations is what will be printed.

### write.undrline()
write.undrline() is near the same as write.console(), ill show you an example: write.undrline("Hello, World!") which would print "<ins>Hello, World!</ins>" thats all you need to know since its near the same as write.console() but it underlines.

### write.bold()
write.bold() is also near the same as write.console(), heres an example: write.bold("Hello, World!") which would print "__Hello, World!__" just the same as the others but it bolds.

### extras
This explanation wont be too long. there are currently two things you can change which are color and the end, the available colors are purple, cyan, darkcyan, blue, green, yellow, and red. And the end one is just end on print.

## The message function
### message.info()
message.info() prints an info message box. Example: message.info("Hello, World!") (i cant show what it would print because it doesnt really let me)

### message.warn()
message.warn() prints a warning message box. Example: message.info("Hello, World!")

### message.err()
message.err() prints an error message box. Example: message.err("Hello, World!")
