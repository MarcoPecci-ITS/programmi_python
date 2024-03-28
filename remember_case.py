frase_iniziale = 'Frase con MAIUSCOLE e minuscole.'
print(f'1) {frase_iniziale}')
frase = list(frase_iniziale)


posizione_maiuscole = []
for posizione, lettera in enumerate(frase):
    if lettera.isupper() is True:
        posizione_maiuscole.append(posizione)


frase2 = frase_iniziale.lower()
print(f'2) {frase2}')
frase2 = list(frase2)
frase_finale = []


for posizione, lettera in enumerate(frase2):
    if posizione in posizione_maiuscole:
        new_letter = lettera.upper()
        frase_finale.append(new_letter)
    else:
        frase_finale.append(lettera)


frase3 = ''.join(frase_finale)
print(f'3) {frase3}')