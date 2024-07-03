# __init__ method

class person:
  def __init__ (self, name, age, gender): # __init__ is constructor , use to initialize the object, it is pre-defined, first complier search for it if class isz defined
    self.name = name # this is written for assining memory location
    self.age = age # this is written for memory location
    self.gender = gender
  def show_details(self):
    print("the name is ",self.name,", age is ",self.age,"and gender is ",self.gender)


# creating object
p1 = person('nimit',35,'male')
p1.show_details()