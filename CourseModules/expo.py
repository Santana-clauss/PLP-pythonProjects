def modular_exponentiation(base, exponent, modulus):
    x = 1
    power = base % modulus
    binary_exponent = bin(exponent)[2:]

    for i in (binary_exponent):
        x = (x * x) % modulus
        if i == '1':
         x = (x * power) % modulus

    return x

base=int(input("Enter your base number :"))
exponent = int(input("Enter your exponent :"))
modulus = int(input("Enter your modulus :"))


result = modular_exponentiation(base, exponent, modulus)
print(f"The result of {base}^{exponent} mod {modulus} is: {result}")