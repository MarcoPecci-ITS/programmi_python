# HEROQUEST LANCIO DADI 3.0
import random
combat_dice = {'Teschio' : 0, 'Scudo Eroe' : 0, 'Scudo Mostro' : 0}


while True:
    user_input = input().lower()
    try:
        quanti_dadi = int(''.join([n for n in user_input if n.isdigit()]))
    except ValueError:
        quanti_dadi = 2
    
    lancio = [random.randint(1, 6) for _ in range(quanti_dadi)]

    if 'm' in user_input:
        print(f'Movimento -> {sum(lancio)}\t{lancio}')
        
    elif 'c' in user_input:
        for dado in lancio:
            if dado in [1, 2, 3]:
                combat_dice['Teschio'] += 1
            elif dado in [4, 5]:
                combat_dice['Scudo Eroe'] += 1
            elif dado == 6:
                combat_dice['Scudo Mostro'] += 1
            
        print('Combattimento -> ', end = '')
        for nome, numero in combat_dice.items():
            print(f'{nome}: {numero}' if numero > 0 else '', end = ' ')
        
        print()
        combat_dice.update({'Teschio' : 0, 'Scudo Eroe' : 0, 'Scudo Mostro' : 0})
        
    else:
        print('Inserire tipo di lancio e numero di dadi: es 4c o m2')