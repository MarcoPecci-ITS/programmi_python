coin_denominations = [500, 100, 25, 10, 5, 1]


while True:
    prelievo = int(input('--- BANCOMAT --- Inserire quantità da prelevare: '))
    for amount in coin_denominations:
        number_of_banknotes = prelievo // amount

        if number_of_banknotes > 0:
            prelievo -= number_of_banknotes * amount
            print(f'{number_of_banknotes} banconote da {amount} $')