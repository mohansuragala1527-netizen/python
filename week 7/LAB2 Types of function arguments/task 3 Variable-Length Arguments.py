#lab2 task3
def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
total, average = total_marks(80, 70, 90)
print("3 Marks - Total:", total, "Average:", average)
total, average = total_marks(80, 70, 90, 85, 75)
print("5 Marks - Total:", total, "Average:", average)
total, average = total_marks(95)
print("1 Mark - Total:", total, "Average:", average)
