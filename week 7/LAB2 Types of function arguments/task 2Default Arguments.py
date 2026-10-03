def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price
print("Price 1:", calculate_price(1000))
print("Price 2:", calculate_price(1000, 10))
print("Price 3:", calculate_price(1000, 10, 100))
