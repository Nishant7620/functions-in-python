
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
