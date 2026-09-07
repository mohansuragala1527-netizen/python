#C2.10.Find highest and lowest priced items.
prices = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5
}

highest = max(prices, key=prices.get)
lowest = min(prices, key=prices.get)

print("Highest Price Item:", highest, "=", prices[highest])
print("Lowest Price Item:", lowest, "=", prices[lowest])
