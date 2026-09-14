#index occurence of a character
string = input("Enter a string: ")
ch = input("Enter a character: ")

first = string.find(ch)
last = string.rfind(ch)

if first != -1:
    print("First occurrence:", first)
    print("Last occurrence:", last)
else:
    print("Character not found")
