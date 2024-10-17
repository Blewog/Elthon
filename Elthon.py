# Global variables
global bold
global underline
global end

bold = '\033[1m'
underline = '\033[4m'
end = '033[0m'

class write:
  def console(text, option):
    if(option != "return"):
      print(bold + text + end, end=option)
    else:
      print(underline + text + end)
