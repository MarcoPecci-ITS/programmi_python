import math, time
start = time.perf_counter()
limite = 100_000


def is_prime(numero):
    for divisore in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisore == 0:
            return False
    return True


numeri_primi = [n for n in range(2, limite + 1) if is_prime(n)]

print(numeri_primi)

end = time.perf_counter()
print(f'\n{len(numeri_primi)} numeri primi trovati in {round(end - start, 3)} secondi')
# 0,098 secondi per 100_000 numeri
# 2_745_694 operazioni eseguite