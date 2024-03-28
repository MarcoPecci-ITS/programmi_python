while True:
    
    print('Inserire un numero:', end = ' ')
    n = input()

    def add_ten(n):
        print(n + 10)

    try:
        add_ten(int(n))
        break

    except (TypeError, NameError, ValueError):
        print('Invalid Input')