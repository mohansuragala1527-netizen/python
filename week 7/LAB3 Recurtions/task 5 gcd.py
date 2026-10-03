#lab3 task5
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD =", gcd(a, b))
print("LCM =", lcm(a, b))
