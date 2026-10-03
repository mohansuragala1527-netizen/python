#lab6 task2
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


numbers = range(1, 51)

primes = list(filter(is_prime, numbers))

print("Prime numbers:", primes)


def is_palindrome(word):
    return word == word[::-1]


words = ["madam", "hello", "level", "python", "radar"]

palindromes = list(filter(is_palindrome, words))

print("Palindromes:", palindromes)
