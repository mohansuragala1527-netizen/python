#lab2 task4
def build_profile(**details):
    print("----- PROFILE -----")
    for key, value in details.items():
        print(key.capitalize() + ":", value)
    print("-------------------")
build_profile(name="Mohan", age=19, city="Rajam", hobby="Cricket")
print()
build_profile(name="Sri", age=20, city="rajam")
