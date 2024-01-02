
x =lambda  name : print(name)

x("Nishant")

#---------------------------------------------------------------------------

add = lambda a,b : a+b

result = add(5,3)
print(result)

#---------------------------------------------------------------------------

calculation = lambda a,b:(a+b,a-b,a*b)

result = calculation(5,3)
print(result)

#----------------------------------------------------------------------------
#storing result in varriable

calc  = lambda a,b:(a+b,a*b,a-b)

x,y,z = calc(5,3)

print(x)
print(y)
print(z)

#--------------------------------------------------------------------------
# passing default argument to lambda function

cal = lambda a,b=5:(a/b)

result = cal(10)
print(result)

#-------------------------------------------------------------------------
#nested lambda function

nested = lambda y :lambda z :(y+z)

result = nested(5)
print(result(3))

#----------------------------------------------------------------------------

nested  = lambda x:(lambda y:(lambda z:(x+y+z)))

p = nested(5)
q = p(3)
r = q(2)

print(r)

#----------------------------------------------------------------------------------
#above function also can be written as:
nested  = lambda x:(lambda y:(lambda z:(x+y+z)))

p = nested(5)(3)(2)
print(p)

#---------------------------------------------------------------------------------
#passing lambda function to another function

def mul(lamb):
    print(f"the result of lambda function {lamb(5,3)}")

lamb = lambda a,b:a*b
mul(lamb)

#----------------------------------------------------------------------------------
#returning lambda function from another function

def power_function(exponent):
    return lambda x:x**exponent


sqr = power_function(2)(5)            #sqr = power_function(2)
print(sqr)                            #sqr(5)                  
                                      #print(sqr)          

#---------------------------------------------------------------------------------------

def calculation(operation):
    if operation =="add":
        return lambda x,y:x+y
    elif operation =="sub":
        return lambda x,y:x-y
    else:
        return lambda x,y:x*y

calc = calculation("add")
result = calc(5,3)
print(result)            