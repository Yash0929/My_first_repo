# Class program

class Greet():
    course = "Python for beginners"  #Class attribute
    def greet_user(self):
        print("Hello User")
    def hello(self):
        print("I am Yash")

# Creating a local object & instantiation a class object
wish = Greet()
wish.greet_user()
wish.hello()
print(wish.course)  