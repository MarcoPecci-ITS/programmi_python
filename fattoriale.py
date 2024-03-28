def fattoriale(n):
    risultato = 1
    for numero in range(2, n + 1):
        risultato *= numero
    return risultato


for x in range(1, 15):
    print(f'{x}!\t-->\t{fattoriale(x)}')