from funzioni import cypher, decypher

alfabeto = list('abcdefghijklmnopqrstuvwxyz')

while True:
    user_choice = input('Vuoi cifrare (c) o decifrare (d) un messaggio? ')
    if user_choice not in ['c', 'd']:
        continue
    messaggio_iniziale = input('Inserire il messaggio: ').lower()
    chiave = input('Inserire una parola da usare come chiave: ').lower()
    while chiave.isalpha() is False:
        chiave = input('La chiave deve essere una parola: ').lower()
    chiave = list(chiave)

    codice_cifratura = []
    for item in chiave:
        codice_cifratura.append(ord(item) - 97)
        # Le lettere della chiave vengono convertite nella loro posizione nell'alfabeto

    messaggio_cifrato = []
    next_code = 0
    # Contatore per usare le lettere della chiave con chiave[next_code], es. chiave[0] è la prima lettera

    for lettera in messaggio_iniziale:
        if lettera not in alfabeto:
            messaggio_cifrato.append(lettera)
            continue
        if next_code > len(codice_cifratura) - 1:
            next_code = 0
            # Se sono finite le lettere nella chiave ricomincia da capo
        
        if user_choice == 'c':
            nuova_lettera = cypher(lettera, int(codice_cifratura[next_code]))
        elif user_choice == 'd':
            nuova_lettera = decypher(lettera, int(codice_cifratura[next_code]))
        
        messaggio_cifrato.append(nuova_lettera)
        next_code += 1

    messaggio_finale = ''.join(messaggio_cifrato)
    print(f'\n{messaggio_iniziale} --> {messaggio_finale}\n')