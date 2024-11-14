# Class constructors

# There are 2 types
# Default constructor
#parameterised constructor

class Hari:
    #Default constructor
    def __init__(self):
        self.course ="Python course"

    #Method to access data members of default constructor
    def access(self):
        print(self.course)

obj = Hari()
obj.access()