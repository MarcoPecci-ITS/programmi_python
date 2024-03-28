lista = ['x', 'z', 'c', 'f', 'a', 'm', 'i', 'b', 'y', 'e', 'u', 'k', 'd']

lista.sort()
for lettera in lista:
    print(lettera, end = ' ')

print()

lista2 = sorted(lista, reverse = True)
for lettera in lista2:
    print(lettera, end = ' ')

#.sort() modifica la lista, sorted() ne crea una nuova senza sostituire l'originale