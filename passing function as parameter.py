def display(sh):
    return "this is display function " + sh


def show():
    return "this is show function"


print(display(show()))

#-----------------------------------------------------------------------------------

def add(x,y):
    return x+y

def mul(x,y):
    return x*y


def operation(operate,x,y):
    return operate(x,y)

result = operation(add,5,3)

print(result)

result2 = operation(mul,5,3)
print(result2)   