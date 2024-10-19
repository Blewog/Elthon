

class write:
  def console(text, option):
    if(option != "return"):
      print(text, end=option)
    else:
      print(text)
  def undrline(text, option):
    if(option != "return"):
      print('{:s}'.format('\u0333').join(text), end=option)
