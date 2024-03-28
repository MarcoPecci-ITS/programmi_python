import random
print('GIOCO: Devi indovinare un numero di 3 cifre, ti darò degli indizi.')
tentativi_rimasti = 10

while True: # il numero deve avere 3 cifre tutte diverse
    numero = str(random.randint(100, 1000))
    numero_da_indovinare = list(numero)
    if len(set(numero_da_indovinare)) == len(numero_da_indovinare):
        break

while True:
    
    lista_guess = list(input('Inserisci numero: '))
    if len(lista_guess) != len(numero_da_indovinare):
        print(f'Il numero ha {len(numero_da_indovinare)} cifre.')
        continue
    
    correct_position, wrong_position = 0, 0
    
    for i in range(len(numero_da_indovinare)):
        if lista_guess[i] == numero_da_indovinare[i]:
            #Cifra esatta, posizione esatta
            correct_position += 1
        elif lista_guess[i] in numero_da_indovinare:
            #Cifra esatta, posizione sbagliata
            wrong_position += 1
    if correct_position == 3:
        print('\nHai indovinato!', end = ' ')
        break
    elif correct_position != 0 or wrong_position != 0:
        print(f'Cifre esatte nella posizione esatta: {correct_position}')
        print(f'Cifre esatte nella posizione sbagliata: {wrong_position}')
    else:
        print('Nessuna cifra è corretta.')

    tentativi_rimasti -= 1
    if tentativi_rimasti <= 0:
        print(f'\nHai perso.', end = ' ')
        break
    
print(f'Il numero era {int(numero)}.')