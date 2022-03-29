class Component:
  def __init__(self, name):
      self.name = name
  
  def execute(self):
    print('function {self.name}() { return "name" } export ${self.name}')