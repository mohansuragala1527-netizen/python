#b3.11.Modify a nested list inside a tuple.
data = ("Python", [10, 20, 30])

data[1].append(40)

print("Tuple:", data)

# The tuple itself is immutable, but the nested list is mutable.
