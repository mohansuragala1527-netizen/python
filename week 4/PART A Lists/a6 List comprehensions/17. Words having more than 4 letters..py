#a6.17. Words having more than 4 letters.
words = ["cat", "apple", "book", "computer", "pen", "python"]

result = [word for word in words if len(word) > 4]

print("Words with more than 4 letters:", result)
