def factorial(num):
    if num==0 or num ==1:
        return 1

    else:

     return  num * factorial(num-1)

num = 5
print(f" factorical of a number {num} is: {factorial(num)}")

#--------------------------------------------------------------------------------

def fibonacci(n):
    if n <=1:
        return n

    else:
        return  fibonacci(n-1)+ fibonacci(n-2)    
n = 5
print(f"Fibonacci series of {n} is: {fibonacci(5)}")