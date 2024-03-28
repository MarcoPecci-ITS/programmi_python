numeri = input('Inserire i numeri da sommare, separati da uno spazio: ').split()

numeri = [int(num) for num in numeri]
print(f'Somma: {sum(numeri)}')