import random
print('--- Prova a indovinare un numero di 3 cifre, ti darò degli indizi ---')
numero_di_tentativi = 10


def generate_number():
    while True:
        n = random.randint(100, 1000)
        if len(set(str(n))) == len(list(str(n))):
            return n


def check_digits():
    correct, wrong_position = 0, 0
    
    for i in range(cifre):
        if user_choice[i] == numero_da_indovinare[i]:
            #Cifra esatta, posizione esatta
            correct += 1
        elif user_choice[i] in numero_da_indovinare:
            #Cifra esatta, posizione sbagliata
            wrong_position += 1
            
    if correct == 3:
        print(f'\nHai indovinato! Era proprio {numero}!')
        return True

    if correct != 0:
        print(f'Cifre esatte nella posizione esatta: {correct}')
    if wrong_position != 0:
        print(f'Cifre esatte nella posizione sbagliata: {wrong_position}')
    if correct == 0 and wrong_position == 0:
        print('Nessuna cifra è corretta.')


while True:
    numero = generate_number()
    numero_da_indovinare = list(str(numero))
    cifre = len(numero_da_indovinare)
    
    for tentativi in range(numero_di_tentativi):
        
        user_choice = list(input('Inserisci numero: '))
        
        if len(user_choice) != cifre:
            print(f'Il numero ha {cifre} cifre.')
            continue
        if len(set(user_choice)) != len(user_choice):
            print(f'Le cifre non si ripetono, sono tutte diverse')
            continue
        
        if check_digits():
            has_won = True
            break
        else:
            has_won = False
        
        print()
    
    if has_won:
        break
    else:
        print(f'Hai perso. Il numero era {numero}.')
        break