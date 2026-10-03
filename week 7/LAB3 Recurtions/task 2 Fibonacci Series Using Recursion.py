#lab3 task2
count = 0
def fibonacci(n):
    global count
    if n == 5:
        count += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("First 15 Fibonacci terms:")
for i in range(15):
    print(fibonacci(i), end=" ")
count = 0
fibonacci(10)
print("\n\nfibonacci(5) is recomputed", count, "times while calculating fibonacci(10).")
