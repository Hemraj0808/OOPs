# Types of method :
# 1. Instance methods
# 2. class methods
# 3. static methods


# class method
class student:

  counter = 0

  def __init__(self,name, marks):
    self.name = name
    self.marks = marks
    student.counter += 1

  def msg(self):
    print("Hello",self.name, "you got",self.marks, "%marks")

  @classmethod
  def object_count(cls):
    return cls.counter

s1 = student("abhishek",65)
s2 = student("amit",89)
print(student.object_count())
print(s1.object_count())
