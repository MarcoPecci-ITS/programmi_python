alunni = {'Carlo': 18, 'Francesco': 20, 'Marco': 21, 'Alex': 19, 'Sara': 18, 'Veronica': 22, 'Giulia': 19, 'Beatrice': 23}

ordine_alfabetico = dict(sorted(alunni.items())) #senza dict() ritorna una lista
ordine_anagrafico = dict(sorted(alunni.items(), key = lambda x: x[1]))


[print(name, ':', age) for name, age in ordine_alfabetico.items()] #list comprehension, equivale al ciclo for in basso

print()

for name, age in ordine_anagrafico.items():
    print(f'{name} : {age}')