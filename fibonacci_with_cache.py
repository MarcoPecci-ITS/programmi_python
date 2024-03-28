from functools import lru_cache

@lru_cache(maxsize= None)
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(0, 500):
    print(f'{fibonacci(n)}')