import time

with (open('alba_tramonto_san_dona.txt', 'r') as file):
    giorni = file.read().split('\n')


def get_alba_tramonto(data):
    for line in giorni:
        if data in line:
            info_giorno = line.split(' ')
            # [giorno_settimana, gg_mm_aa, alba, tramonto, ore_di_luce, solare_legale]

            return f'{data} ---> Alba {info_giorno[2]} | Tramonto {info_giorno[3]}'


def main():
    data_odierna = time.strftime('%d/%m')
    print(f'-Orari di alba e tramonto a San Donà di Piave-\n{get_alba_tramonto(data_odierna)}')

    while True:
        data = input('\nInserisci una data gg/mm o scrivi "exit" per uscire: ')
        if data.lower() == 'exit':
            break
        elif len(data) != 5:
            continue
        print(get_alba_tramonto(data))


if __name__ == "__main__":
    main()
