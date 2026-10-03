#lab6 task1
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


temperatures = [0, 10, 20, 30, 40]

fahrenheit = list(map(celsius_to_fahrenheit, temperatures))

print("Celsius:", temperatures)
print("Fahrenheit:", fahrenheit)


def to_uppercase(text):
    return text.upper()


words = ["python", "java", "c", "html"]

upper_words = list(map(to_uppercase, words))

print("Original:", words)
print("Uppercase:", upper_words)
