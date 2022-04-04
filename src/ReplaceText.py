import fileinput
import sys

class ReplaceText:
  def __init__(self, file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=True):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)