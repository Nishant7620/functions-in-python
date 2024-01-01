# nested function with return statement

def outer():
    def inner():
        return "inner function"
    return "outer function" " " + inner() 

x = outer()
print(x)
