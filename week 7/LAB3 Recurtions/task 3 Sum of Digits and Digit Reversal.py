#lab3 task3
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)
n = int(input("Enter a positive number: "))
print("Sum of digits:", sum_of_digits(n))
print("Reversed number:", reverse_number(n))
