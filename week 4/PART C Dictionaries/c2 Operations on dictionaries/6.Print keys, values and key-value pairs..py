#c2.6.Print keys, values and key-value pairs.
student = {
    "name": "MOHAN",
    "age": 19,
    "course": "CSE"
}

print("Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)
