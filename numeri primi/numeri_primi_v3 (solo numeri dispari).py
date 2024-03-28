import math, time
start = time.perf_counter()
limite = 100_000


def is_prime(numero):
    for divisore in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisore == 0:
            return False
    return True


numeri_primi = [n for n in range(3, limite + 1, 2) if is_prime(n)]

if is_prime(2):
    numeri_primi.insert(0, 2)
    
print(numeri_primi)

end = time.perf_counter()
print(f'\n{len(numeri_primi)} numeri primi trovati in {round(end - start, 3)} secondi')
# 0,081 secondi per 100_000 numeri
# 2_695_695 operazioni eseguite