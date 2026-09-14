#25. Own version of str.find and count
s = input("Enter a string: ")
sub = input("Enter substring: ")

# Own find()
position = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        position = i
        break

# Own count()
count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count += 1

print("Find position:", position)
print("Count:", count)
