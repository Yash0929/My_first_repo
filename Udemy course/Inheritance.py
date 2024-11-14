# Inheritance
#Parent class
class Mammal:
    def walk(self):
        print("walk")

#Child class
class Dog(Mammal):
    pass

#Child class
class Cat(Mammal):
    pass

class tiger(Mammal):
    def gandu(self):
        print("I am the king")



obj = Dog()
print (obj.walk())
obj_1= tiger()
print (obj_1.gandu())


