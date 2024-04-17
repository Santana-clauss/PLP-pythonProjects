def bezout(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = bezout(b, a % b)
        return gcd, y, x - (a // b) * y

# Example 
num1 = 486
num2 = 222
gcd, x, y = bezout(num1, num2)
print("GCD:", gcd)
print(f"Bezout coefficients:\nx = {x}\ny = {y}")

