# This is my first class

class car:
    model = 'EOS'
    HP = 122
    brand = 'Volkswagen'

    def acc(self,acc):
        self.accelerate= acc

    def cal_kw(self):
        self.kw= round(0.735499*self.HP,2)
        return self.kw

SUV = car()
SUV.HP=155
print(SUV.cal_kw())
