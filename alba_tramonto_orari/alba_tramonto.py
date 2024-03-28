import time

data_oggi = time.strftime('%d/%m')

with open('alba_tramonto_san_dona.txt', 'r') as file:
    full_text = file.read()
    lista_giorni = full_text.split('\n')


def alba_tramonto(data):
    
    for line in lista_giorni:
        if data in line:
            informazioni = line.split(' ')
            # [giorno_settimana, gg_mm_aa, alba, tramonto, ore_di_luce, solare_legale]
            
            alba, tramonto = informazioni[2], informazioni[3]
            print(f'{data} --->  Alba {alba} | Tramonto {tramonto}')
            break


print('Orari di alba e tramonto a San Donà di Piave')
alba_tramonto(data_oggi)

while True:
    data = input('\nInserisci una data gg/mm: ')
    if data == '':
        break
    elif len(data) != 5:
        continue
    alba_tramonto(data)