#lab7 task6
import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)

        result = func(*args, **kwargs)

        print("Returned:", result)
        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution time:", end - start, "seconds")
        return result

    return wrapper


@log_call
@timer
def add(a, b):
    return a + b


print("Result:", add(10, 20))
