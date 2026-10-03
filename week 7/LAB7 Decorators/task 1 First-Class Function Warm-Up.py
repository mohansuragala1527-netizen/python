#lab7 task1
def greet(name):
    return "Hello " + name


# (a) Assign function to another variable
new_greet = greet
print(new_greet("siri"))


# (b) Pass function as an argument
def display(func, name):
    print(func(name))

display(greet, "hasi")


# (c) Return a function from another function
def create_greeting():
    def message():
        return "Welcome to Python!"

    return message


my_function = create_greeting()
print(my_function())
