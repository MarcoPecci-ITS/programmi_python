numeri = input('Inserire i numeri da arrotondare, separati da uno spazio: ').split()

def arrotonda(x):
    numero, decimali = x.split('.')
    if int(decimali[:1]) < 5:
        return int(numero)
    else:
        return int(numero) + 1

numeri_arrotondati = [arrotonda(numero) for numero in numeri]

for i in range(len(numeri)):
    print(f'{numeri[i]} --> {numeri_arrotondati[i]}')