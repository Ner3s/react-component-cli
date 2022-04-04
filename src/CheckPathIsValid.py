import re

class CheckPathIsValid:
  def execute(path):
    # Check if start with ./ and end with /
    if re.search("^\./", path) and re.search("/$", path): 
      print("Path valid! :D")
    else:
      print("Path invalid!!!, should start with ./ and end with /")
      exit()