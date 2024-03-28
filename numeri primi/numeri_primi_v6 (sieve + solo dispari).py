import math, time
start = time.perf_counter()
limite = 100_000
is_prime = [True] * (limite + 1)


for number in range(2, int(math.sqrt(limite)) + 1):
    if is_prime[number]:
        for multiple in range(number * number, limite + 1, number):
            is_prime[multiple] = False


numeri_primi = [n for n in range(3, limite + 1, 2) if is_prime[n]]
numeri_primi.insert(0, 2)

print(numeri_primi)
end = time.perf_counter()
print(f'\n{len(numeri_primi)} numeri primi trovati in {round(end - start, 3)} secondi')
# 0,01 secondi per 100_000 numeri