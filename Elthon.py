# Global variables
purple = "\033[95m"
cyan = "\033[96m"
darkcyan = "\033[36m"
blue = "\033[94m"
green = "\033[92m"
yellow = "\033[93m"
red = "\033[91m"
end = "\033[0m"

border_char = "*"

# Basically print but with options
class write:
  def console(text, **kwargs):
    color = kwargs.get("color")
    ending = kwargs.get("end")
    color_code = globals().get(color, "")

    if(color): 
      if(ending):
        print(f"{color_code}{text}{end}", end=ending)
      else:
        print(f"{color_code}{text}{end}")
    if(not color and not ending):
      print(text)
  def undrline(text, **kwargs):
    color = kwargs.get("color")
    ending = kwargs.get("end")
    color_code = globals().get(color, "")

    if(color):
      if(ending):
        print(color_code + '{:s}'.format('\u0332'.join(text)) + end, end=ending)
      else:
        print(color_code + '{:s}'.format('\u0332'.join(text)) + end)
  def bold(text, **kwargs):
    color = kwargs.get("color")
    ending = kwargs.get("end")
    color_code = globals().get(color, "")

    if(color):
      if(ending):
        print(f"{color_code}\033[1m{text}\033[0m{end}", end=ending)
      else:
        print(f"{color_code}\033[1m{text}\033[0m{end}")
    if(not color and not ending):
      print("\033[1m" + text + "\033[0m")

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
    print(border_char * box_width)
    print(f"{border_char} \033[1m[ERROR]\033[0m{' ' * (box_width - 10)}{border_char}")
    print(f"{border_char}{' ' * (box_width - 2)}{border_char}")
    print(f"{border_char} {text}{' ' * (box_width - len(text) - 3)}{border_char}")
    print(border_char * box_width)
