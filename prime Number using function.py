num = int(input("Enter a number: "))
def prime(num):
    if num<=1:
        return True

    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True


if prime(num):
    print("prime")

else:
    print("not prime")
prime(num)

#------------------------------------------------------------------------