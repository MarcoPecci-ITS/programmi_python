initial_number = 100

for year in range(41):

    amount_left = initial_number*(0.9)**year
    print(f'{year}: \t{round(amount_left, 1)}')