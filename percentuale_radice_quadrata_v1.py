import math, time
start = time.perf_counter()

def percentage_square(radice, numero):
    
    if radice == int(radice):
        print(f'Radice: {round(radice)}\t numero: {numero}\
\t-> \t{round(radice/numero * 100, 2)}%')

for n in range(1, 10001):
    
    percentage_square(math.sqrt(n), n)
    

end = time.perf_counter()
print(f'\nTempo di esecuzione: {round(end - start, 5)} secondi')
#0,31