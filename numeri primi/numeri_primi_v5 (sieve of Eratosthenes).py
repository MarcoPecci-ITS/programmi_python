import math, time
start = time.perf_counter()
limite = 100_000


is_prime = [True] * (limite + 1)
# Genera una lista con un numero di valori True uguale al limite stabilito

for number in range(2, int(math.sqrt(limite)) + 1):
    if is_prime[number]:
        for multiple in range(number * number, limite + 1, number):
            is_prime[multiple] = False
# I multipli di un numero primo non sono primi, quindi ad essi assegno False

numeri_primi = [n for n in range(2, limite + 1) if is_prime[n]]
# Aggiungi un numero alla lista dei numeri primi solo se non è stato escluso
# dal ciclo precedente

print(numeri_primi)

end = time.perf_counter()
print(f'\n{len(numeri_primi)} numeri primi trovati in {round(end - start, 3)} secondi')
# 0,011 secondi per 100_000 numeri