#task 4.2 Find cat, dog, or bird
import re

s = "I have a cat, dog and bird"
print(re.findall(r"\b(cat|dog|bird)\b", s))
