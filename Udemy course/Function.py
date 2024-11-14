#Function with default parameter value

def greet (name, msz="GM"):
    print("Hello", name,msz)


greet("Yash")
######

#Return keyword in function

def return_kw(a,b):
    return a + b

res = return_kw(5,2)
print(res)
#######

#Method Over loading

def OL(a,b):
    return a * b

res = OL(5,2)
print(res)

