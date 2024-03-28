import time
start = time.perf_counter()
limite = 100_000


def is_prime(numero):
    for divisore in range(2, numero//2 + 1):
        if numero % divisore == 0:
            return False
    return True


numeri_primi = [n for n in range(2, limite + 1) if is_prime(n)]

print(numeri_primi)

end = time.perf_counter()
print(f'\n{len(numeri_primi)} numeri primi trovati in {round(end - start, 3)} secondi')
# 7,6 secondi per 100_000 numeri
# 227_995_678 operazioni eseguite