#lab5 task3
counter = 10

# Without global keyword
def wrong_function():
    counter = counter + 1
    print(counter)

try:
    wrong_function()
except UnboundLocalError:
    print("Error: UnboundLocalError")

# Fixed function
def correct_function():
    global counter
    counter = counter + 1
    print("Counter after fixing:", counter)

correct_function()
