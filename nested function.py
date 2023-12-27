def outer():
    def inner():
        print("outer function")
    print("inner function")
    inner()
outer()  

#----------------------------------------------------------------------------------
# nested function with return statement

def outer():
    def inner():
        return "inner function"
    return "outer function" " " + inner() 

x = outer()
print(x)

