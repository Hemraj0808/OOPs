# using abc insted of self
class person:
  def __init__(default,name,age):
    default.name = name
    default.age = age
  def myfunc(abc):
    print("hello my name is "+abc.name)

p1 = person("john",36)
p1.myfunc()
