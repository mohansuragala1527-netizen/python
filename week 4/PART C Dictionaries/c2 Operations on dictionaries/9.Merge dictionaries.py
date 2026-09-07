#C2.9.Merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print("Using update():", dict1)

dict3 = {"a": 1, "b": 2}
merged = dict3 | dict2

print("Using | operator:", merged)
