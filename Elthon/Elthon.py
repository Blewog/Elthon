# Any needed modules
import sys
import os

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

current_dir = os.path.dirname(os.path.abspath(__file__))

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
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)
    
    try:
      with open(file_path, "a") as f:
        f.write(f"{text}\n")
    except FileNotFoundError:
      message.err(f"File '{filename}' not found.")
      return None

  def history(**kwargs):
    global file
    custom_file = kwargs.get("file")
    filename = custom_file if custom_file else file
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    try:
      with open(file_path, "r") as f:
        content = f.read()
        return content
    except FileNotFoundError:
      message.err(f"File '{filename}' not found.")
      return None
  
  def clear(**kwargs):
    custom_file = kwargs.get("file")
    filename = custom_file if custom_file else file
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    if(os.path.isfile(file_path)):
      with open(file_path, "w") as f:
        f.write("")
        message.info(f"'{file_path}' cleared successfuly.")
    else:
      message.err(f"File '{file_path}' not found.")
      return None

# Takes input and returns it
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

# used for messing with files
class files():
  def read(file):
    filename = file
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    try:
      with open(file_path, "r") as f:
        content = f.read()
        return content
    except FileNotFoundError:
      message.err(f"File '{filename}' not found.")
      return None
    
  def write (text, file):
    filename = file
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    if(os.path.isfile(file_path)):
      with open(file_path, "a") as f:
        f.write(f"{text}\n")
    else:
      message.err(f"File '{file_path}' not found.")
      return None

  def clear(file):
    filename = file
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    if(os.path.isfile(file_path)):
      with open(file_path, "w") as f:
        f.write("")
        message.info(f"'{file_path}' cleared successfuly.")
    else:
      message.err(f"File '{file_path}' not found.")
      return None

  def create(name, **path):
    filename = path
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    if(not os.path.isfile(file_path)):
      with open(file_path, "w") as f:
        message.info(f"'{file_path}' created successfuly.")
    else:
      message.warn(f"File '{file_path}' already exists.")
  
  def delete(path):
    filename = path
    if(os.path.isabs(filename)):
      file_path = filename
    else:
      file_path = os.path.join(os.path.dirname(current_dir), filename)

    if(os.path.isfile(file_path)):
      try:
        os.remove(file_path)
        message.info(f"'{file_path}' deleted successfuly.")
      except Exception as e:
        message.err(f"Error deleting '{file_path}': {e}")
    else:
      message.err(f"File '{file_path}' not found.")

    if(not os.path.isfile(file_path)):
      with open(file_path, "w") as f:
        message.info(f"'{file_path}' created successfuly.")
    else:
      message.warn(f"File '{file_path}' already exists.")
