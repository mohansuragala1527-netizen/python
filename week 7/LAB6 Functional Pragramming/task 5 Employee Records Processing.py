#lab6 task5
from functools import reduce

employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Sita", "department": "HR", "salary": 35000},
    {"name": "Amit", "department": "IT", "salary": 50000},
    {"name": "Rahul", "department": "Sales", "salary": 30000}
]

# Select IT employees
it_employees = filter(
    lambda e: e["department"] == "IT",
    employees
)

# Give 10% salary hike and create new dictionaries
hiked_employees = list(
    map(
        lambda e: {
            "name": e["name"],
            "department": e["department"],
            "salary": e["salary"] * 1.10
        },
        it_employees
    )
)

# Calculate total salary
total_salary = reduce(
    lambda a, b: a + b["salary"],
    hiked_employees,
    0
)

print("IT Employees after 10% hike:")

for e in hiked_employees:
    print(e)

print("Total Salary Expenditure:", total_salary)
