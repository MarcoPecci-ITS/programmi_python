numeri = input('Inserire i numeri da arrotondare, separati da uno spazio: ').split()

numeri_arrotondati = [round(float(numero)) for numero in numeri]

for i in range(len(numeri)):
    print(f'{numeri[i]} --> {numeri_arrotondati[i]}')