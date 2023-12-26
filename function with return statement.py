def display():
    return "this is display function"

print(display())

#------------------------------------------------------------------------------

def add(a,b):
    return a+b

print(add(8,2))    

#------------------------------------------------------------------------------
#function returning to variable

def cal(a,b):
    return a+b ,a-b
x,y = cal(5,3)

print(x,y)

