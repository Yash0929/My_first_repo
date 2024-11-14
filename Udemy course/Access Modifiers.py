#Access modifiers
# Public , protected & private
from Methods import greet


class Greet:
    #public data member
    var1 = None

    #protected data member
    _var2 = None

    #private data member
    __var3 = None

    #class constructor
    def __int__(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    #public member function
    def accessPublicMembers(self):
        print("Public data member:",self.var1)


    #protected member data
    def _accessProtectedMembers(self):
        print("Protected Data Members:",self._var2)

    #private data member
    def __accessPrivateMembers(self):
        print("Private Data Members:",self.__var3)

# Child class or derived class

class Sub(Greet):
    #Constructor
    def __int__(self,var1,var2,var3):
        greet.__init__(self, var1,var2, var3)

    def ProtectedMembers(self):
        self._accessProtectedMembers()


obj = Sub ()
obj.accessPublicMembers()
obj.ProtectedMembers()





