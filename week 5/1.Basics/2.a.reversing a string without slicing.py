#2.reversing a string without slicing
string = input("Enter a string: ")

reverse = ""

for i in range(len(string) - 1, -1, -1):
    reverse = reverse + string[i]

print("Reversed string:", reverse)
