# Any needed modules
import sys

# Global variables
purple = "\033[95m"
cyan = "\033[96m"
darkcyan = "\033[36m"
blue = "\033[94m"
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
end = "\033[0m"

file = "SaveFunctionHistory.txt"
history = []
space = " "
border_char = "*"

# Basically print but with options
class write:
  def console(text, **kwargs):
    sHistory = kwargs.get("history")
    color = kwargs.get("color")
    ending = kwargs.get("end")
    color_code = globals().get(color, "")

    if(color): 
      if(ending):
        print(f"{color_code}{text}{ending}{end}", end="")
      else:
        print(f"{color_code}{text}{end}")
      if(sHistory):
        print(f"{color_code}{', '.join(history)}{end}")
    else:
      if(ending):
        print(f"{text}{ending}", end="")
    if(not color and not ending):
      if(sHistory):
        pHistory = save.history()
        print(', '.join(pHistory))
      else:
        print(text)
  
  def undrline(text, **kwargs):
    color = kwargs.get("color")
    ending = kwargs.get("end")
    color_code = globals().get(color, "")

    if(color):
      if(ending):
        print(color_code + '{:s}'.format('\u0332'.join(text)) + ending + end, + end, end="")
      else:
        print(color_code + '{:s}'.format('\u0332'.join(text)) + end)
    else:
      if(ending):
        print(f"{text}{ending}", end="")
    if(not color and not ending):
      print(text)
      
  def bold(text, **kwargs):
    color = kwargs.get("color")
    ending = kwargs.get("end")
    color_code = globals().get(color, "")

    if(color):
      if(ending):
        print(f"{color_code}\033[1m{text}\033[0m{end}", end=ending)
      else:
        print(f"{color_code}\033[1m{text}\033[0m{end}")
    else:
      print(f"\033[1m{text}{ending}\033[0m", end="")
    if(not color and not ending):
      print("\033[1m" + text + "\033[0m")

# Prints a message box
class message:
  def info(text):
    box_width = len(text) + 8

    print(border_char * box_width)
    print(f"{border_char} \033[1m[INFO]\033[0m{' ' * (box_width - 9)}{border_char}")
    print(f"{border_char}{' ' * (box_width - 2)}{border_char}")
    print(f"{border_char} {text}{' ' * (box_width - len(text) - 3)}{border_char}")
    print(border_char * box_width)
  
  def warn(text):
    box_width = len(text) + 8

    print(border_char * box_width)
    print(f"{border_char} \033[1m[WARNING]\033[0m{' ' * (box_width - 12)}{border_char}")
    print(f"{border_char}{' ' * (box_width - 2)}{border_char}")
    print(f"{border_char} {text}{' ' * (box_width - len(text) - 3)}{border_char}")
    print(border_char * box_width)

  def err(text):
    box_width = len(text) + 8

    print(border_char * box_width)
    print(f"{border_char} \033[1m[ERROR]\033[0m{' ' * (box_width - 10)}{border_char}")
    print(f"{border_char}{' ' * (box_width - 2)}{border_char}")
    print(f"{border_char} {text}{' ' * (box_width - len(text) - 3)}{border_char}")
    print(border_char * box_width)

# Essentially a clipboard
class save():
  def text(text, **SaveOptions):
    global file
    custom_file = SaveOptions.get("file")
    filename = custom_file if custom_file else file
    color = SaveOptions.get("color")
    color_code = globals().get(color, "")
    
    with open(filename, "a") as f:
      if(color):
        f.write(f"{color_code}{text}{end}\n")
      else:
        f.write(f"{text}\n")

  def history(**kwargs):
    global file
    custom_file = kwargs.get("file")
    filename = custom_file if custom_file else file

    with open(filename, "r") as f:
      history = [line.strip() for line in f]
      return history
  
  def clear(**kwargs):
    global file
    custom_file = kwargs.get("file")
    filename = custom_file if custom_file else file

    with open(filename, "w") as f:
      f.write("")

def input(text, **kwargs):
  color = kwargs.get("color")
  color_code = globals.get(color, "")

  if(color):
    write.console(f"{color_code}{text}{end}", end="")
    input = sys.stdin.readline().strip()
    return input
  else:
    write.console(text, end="")
    input = sys.stdin.readline().strip()
    return input
