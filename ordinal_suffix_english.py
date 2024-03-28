def add_suffix(n):
    if n in (11, 12, 13):
        print(f'{n}th')
    elif str(n).endswith('1'):
        print(f'{n}st')
    elif str(n).endswith('2'):
        print(f'{n}nd')
    elif str(n).endswith('3'):
        print(f'{n}rd')
    else:
        print(f'{n}th')

for day in range(1, 32):
    add_suffix(day)