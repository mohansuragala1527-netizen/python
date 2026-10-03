#lab4 task5
items = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000
}

sorted_items = sorted(items.items(), key=lambda x: x[1])

print("Items from cheapest to most expensive:")

for item, price in sorted_items:
    print(item, ":", price)
