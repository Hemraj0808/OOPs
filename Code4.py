# Creating class and object with class  and instance attribute


class Dog:
    # Class attribute
    species = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Object instantiation
rodger = Dog("Rodger")
tommy = Dog("Tommy")

# Accessing class attribute
print(f"Rodger is a ",rodger.species)
print(f"Tommy is also a ",tommy.species)

# Accessing instance attributes
print(f"My name is ",rodger.name)
print(f"My name is ",tommy.name)
