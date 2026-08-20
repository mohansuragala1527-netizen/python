# ex17: prime num b/w two limits
start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))

print("Prime numbers:")

for n in range(start, end + 1):
    if n >= 2:
        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            print(n, end=" ")
