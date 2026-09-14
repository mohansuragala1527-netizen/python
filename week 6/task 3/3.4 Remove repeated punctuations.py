#task3.4 Remove repeated punctuations
import re

s = "Wait!!! What??? Really!!"
result, n = re.subn(r"([!?])\1+", r"\1", s)

print(result)
print("Replacements:", n)
