def gcd(a,b):
    #compute gcd
    while(b!=0):
        a,b=b,a%b
    return a
a=int(input("Enter first number:"))
b=int(input("Enter first number:"))

result = gcd(a, b)


print(f"The greatest common divisor of {a} and {b} is: {result}")