# Abstraction

from abc import ABC,abstractmethod
from symtable import Class


class Car(ABC):
    def milage(self):
        pass

class Tesla(Car):
    def milage(self):
        print("Milage 30 kms perhr")

class Honda(Car):
    def milage(self):
        print("Milage is 50 kmhr")

t = Tesla()
t.milage()

h = Honda()
h.milage()


