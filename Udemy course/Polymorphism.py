# Polymorphism in python

class bulbul:
    def fly(self):
        print("Bulbul can fly")

class ostrich:
    def fly(self):
        print("Ost cannot fly")

#Common interface

def common(trait):
    trait.fly()

#Inistiate class
obj = bulbul()
obj1 = ostrich()

#Passing the object value

common(obj)
common(obj1)

