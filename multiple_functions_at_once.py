import random


def interact(object, *args):
    print(f'Initial_list> {object}')
    for operation in args:
        print(f'{str(operation).replace("<built-in function ", "")}\t {operation(object)}')


for _ in range(3):
    numeri = [random.randint(1, 101) for _ in range(10)]
    interact(numeri, len, max, min, sum, sorted)
    print()