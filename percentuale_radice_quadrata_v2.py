#V2
import math, time
start = time.perf_counter()


for radice in range(1, 101):
    print(f'Radice: {radice}\t Numero: {radice*radice}\
\t-> \t{round(radice/(radice*radice) * 100, 2)}%')


end = time.perf_counter()
print(f'\nTempo di esecuzione: {round(end - start, 3)} secondi')