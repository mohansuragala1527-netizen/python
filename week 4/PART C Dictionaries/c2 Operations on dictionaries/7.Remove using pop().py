#C2.7.Remove using pop()
student = {
    "name": "Ravi",
    "age": 20,
    "course": "CSE"
}

removed = student.pop("age")

print("Removed:", removed)
print("Dictionary:", student)

result = student.get("phone", "Key not found")
print("Phone:", result)
