# Encapsulation

class Lappy:
    def __init__(self):
        self.__maxprice = 2500

    def sell(self):
        print("Selling price:",format(self.__maxprice))

    def setmaxprice(self,price):
        self.__maxprice = price

CVV = Lappy()
CVV.sell()
#updating the price

CVV.__maxprice = 4500
CVV.sell()

#using setter method
CVV.setmaxprice(4500)
CVV.sell()


