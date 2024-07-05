# __str__ method used to return

class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __str__(self): # this will be call when we will print the
    return f"The name is {self.name} and age is {self.age}"

p = person("john",36)
print(p)