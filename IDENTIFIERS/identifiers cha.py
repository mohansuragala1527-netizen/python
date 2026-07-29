# identifiers challenge 
import keyword

def is_valid_identifier(name):
    if len(name) == 0:
        return False

    if not (name[0].isalpha() or name[0] == "_"):
        return False

    for ch in name:
        if not (ch.isalnum() or ch == "_"):
            return False

    if keyword.iskeyword(name):
        return False

    return True

name = input("Enter identifier: ")
print(is_valid_identifier(name))
