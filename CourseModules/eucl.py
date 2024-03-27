def gcd(a,b):
    #compute gcd of 2 integeers using euclidean algorithm
    while(b!=0):
        a,b=b,a%b
    return a
a=int(input("Enter first number:"))
b=int(input("Enter first number:"))

result = gcd(a, b)

# Print the result
print(f"The greatest common divisor of {a} and {b} is: {result}")