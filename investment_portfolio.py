#Questo codice prende un dizionario con una serie di investimenti in ordine casuale e li ordina dal maggiore al minore mostrando la percentuale

investimenti_cliente = {'Apple' : 10_000, 'Microsoft' : 5500, 'Amazon' : 7000,
                         'Samsung' : 3750, 'Google' : 4000, 'Tesla' : 1200}

sorted_portfolio = dict(sorted(investimenti_cliente.items(), key = lambda item: item[1], reverse = True))
#lambda serve a specificare in che ordine mettere gli elementi
#item[1] ordina per values, item[0] per keys

total_invested = sum(sorted_portfolio.values())

for key in sorted_portfolio:
    percentage = round(sorted_portfolio[key] / total_invested * 100, 2)
    print(f'{key}: {percentage}%')