
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
