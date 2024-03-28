from cifra_decifra import encrypt, decrypt

while True:
    user_choice = input('Vuoi cifrare (c) o decifrare (d) un messaggio? ').lower()
    if user_choice not in ['c', 'd']:
        continue
    
    frase = list(input('Inserisci il messaggio: '))
    have_key = input('Hai una chiave segreta(y/n)? ')
    
    while have_key.lower() in ['yes', 'y', 'si', 'sì'] or user_choice == 'c':
        if user_choice == 'c':
            chiave = input('Per cifrare un messaggio serve una chiave: ')
        else:
            chiave = input('Inserisci la chiave: ')
    
        try:
            chiave = int(chiave)
            if -26 <= chiave <= 26:
                break
            else:
                print('ERRORE - come chiave devi scegliere un numero tra -26 e 26!')
                continue
        except (TypeError, ValueError):
            print('ERRORE - come chiave devi scegliere un numero tra -26 e 26!')
            continue
    
    print()

    if user_choice == 'c':
        secret_output = encrypt(frase, chiave)
        
        print(''.join(secret_output))  # Trasformo list in str
        
    elif user_choice == 'd' and have_key.lower() in ['yes', 'y', 'si', 'sì']:
        decoded_output = decrypt(frase, chiave)
        
        print(''.join(decoded_output))
    
    elif user_choice == 'd' and have_key.lower() in ['no', 'n']:
        risultati = []

        for chiave in range(1, 27):
            candidato = decrypt(frase, chiave)
            risultati.append(candidato)

        print('\nBEST RESULTS:')
        for candidato in risultati:
            if 'x' not in candidato and 'y' not in candidato and 'j' not in candidato and 'w' not in candidato and 'k' not in candidato:
                print(f'#{risultati.index(candidato) + 1} --> ', end = '')
                print(''.join(candidato))

        print('\nALL RESULTS:')
        for candidato in risultati:
            print(f'#{risultati.index(candidato) + 1} --> ', end = '')
            print(''.join(candidato))
    
    else:
        continue