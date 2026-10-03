#lab1 task2
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = simple_interest(p, r, t)
print("Simple Interest =", si)
