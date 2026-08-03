# input output statements - challenge
marks = list(map(int, input("Enter 3 subject marks: ").split()))

average = sum(marks) / 3

print("Average = {:.2f}".format(average))
