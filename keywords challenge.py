 # keyword - Challenge

import keyword

print("Soft Keywords:")
for i in keyword.softkwlist:
    print(i)

print("\nHard Keywords:")
for i in keyword.kwlist:
    if i not in keyword.softkwlist:
        print(i)
