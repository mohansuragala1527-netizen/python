#17. reverse the order
sentence = input("Enter a sentence: ")

words = sentence.split()
reverse = words[::-1]

print("Reversed sentence:", " ".join(reverse))
