class Dog:
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def bark(self):
        print(f"{self.name} says woof!")  # instance method

    def get_age(self):
        return self.age  # instance method

    def set_age(self, age):
        self.age = age  # instance method to set a new age

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 5)

# Calling instance methods
my_dog.bark()         
print(my_dog.get_age())  

# Setting a new age
my_dog.set_age(6)
print(my_dog.get_age())  
