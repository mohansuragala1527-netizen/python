#22.duplicate characters and their counts
s = input("Enter a string: ")

for ch in s:
    if s.count(ch) > 1:
        print(ch, ":", s.count(ch))
