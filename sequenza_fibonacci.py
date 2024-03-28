lunghezza_sequenza = int(input('Quanti numeri devo generare? '))
fibonacci = []

for n in range(lunghezza_sequenza + 1):
    if n > 1:
        nuovo_numero = int(fibonacci[n - 1]) + int(fibonacci[n - 2])
        fibonacci.append(nuovo_numero)
    else:
        fibonacci.append(n)

print(fibonacci[1:])