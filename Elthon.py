

# Global variables
global box_width
global border_char

border_char = "*"

class write:
  def console(text, option):
    if(option != "return"):
      print(text, end=option)
    else:
      print(text)
  def undrline(text, option):
    if(option != "return"):
      print('{:s}'.format('\u0332'.join(text), end=option))
    else:
      print('{:s}'.format('\u0332'.join(text)))
  def bold(text, option):
    if(option != "return"):
      print(f'\033[1m{text}\033[0m', end=option)
    else:
      print(f'\033[1m{text}\033[0m')

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
