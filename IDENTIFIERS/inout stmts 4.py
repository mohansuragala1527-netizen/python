# input output statements - program 4
numbers = input("Enter numbers: ").split()

numbers = list(map(int, numbers))

print("Sum =", sum(numbers))
