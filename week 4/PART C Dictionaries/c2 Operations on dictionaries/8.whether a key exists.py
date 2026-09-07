#C2.8.whether a key exists
student = {
    "name": "Ravi",
    "age": 20
}

key = "age"

if key in student:
    print("Value:", student[key])
else:
    print("Key does not exist")
