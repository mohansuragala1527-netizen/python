#lab3 task1
def factorial(n):
    if n < 0:
        return "Factorial not possible for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
n = int(input("Enter a number: "))
print("Recursive Factorial:", factorial(n))
if n >= 0:
    print("Iterative Factorial:", factorial_iterative(n))
