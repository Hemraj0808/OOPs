# class variable and instance variable



class car:
  wheel = 4 # class variable
  def __init__(self,name):
    self.name = name # instance variable

mercedes = car("mercedes")
print(mercedes.wheel) # access of class variable through object
print(car.wheel) # access of class variable through class
print(mercedes.name) # access of instance variable through object
