# roll two six-sided dice; the player has to guess whether the sum is even or odd.
import random

def lancia_dadi():
    scelta = input('Lancerò due dadi con sei facce. Indovina se la somma sarà pari o dispari: ')


    results = [random.randint(1, 7) for i in range(2)]
    '''
    list comprehension, equivalente a:
    results = []
    for i in range(2):
        results.append(random.randint(1, 7))
    '''

    somma = sum(results)
    print(f'Primo dado: {results[0]} | Secondo dado: {results[1]}\nSomma: {somma}')

    if scelta == 'pari' and somma % 2 == 0:
        print('Hai vinto!')
    elif scelta == 'dispari' and somma % 2 != 0:
        print('Hai vinto!')
    else:
        print('Hai perso.')

lancia_dadi()