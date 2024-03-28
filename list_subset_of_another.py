import string

alphabet = set(string.ascii_lowercase)

some_letters = set(['a', 's', 'x', 'a'])

print(some_letters.issubset(alphabet))