#lab4 task3
students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]

# Sort by marks in descending order
sorted_students = sorted(
    students,
    key=lambda s: s[1],
    reverse=True
)

print("Students sorted by marks:")
print(sorted_students)


# Sort strings by length
names = ["Rahul", "Amit", "Sita", "Krishna"]

sorted_names = sorted(names, key=lambda x: len(x))

print("\nNames sorted by length:")
print(sorted_names)
