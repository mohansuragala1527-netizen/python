#C2.11.Character frequency in a string.
text = "hello"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:", frequency)
