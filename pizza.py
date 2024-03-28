import time
base_price = 5


def make_pizza(size, *toppings):
    display = 'Pizza ' + size + ' con '
    for ingrediente in toppings:
        if toppings.index(ingrediente) == len(toppings) - 1:
            display = display + ingrediente
        else:
            display = display + ingrediente + ', '
    print(display, end = '')

    price = base_price
    if size == 'grande':
        price += 1.5
    for ingrediente in toppings:
        price += 1

    price = str(price) + '€'
    print(price.rjust(70 - len(display), '_'))


start = time.perf_counter_ns()

make_pizza('media', 'patatine')
make_pizza('grande', 'speck', 'asiago')
make_pizza('grande', 'prosciutto', 'funghi')
make_pizza('media', 'pomodorini', 'feta', 'olive')
make_pizza('media', 'mozzarella', 'basilico')
make_pizza('grande', 'salame', 'gorgonzola')
make_pizza('media', 'prosciutto', 'rucola')
make_pizza('media', 'pomodoro', 'mozzarella', 'origano')
make_pizza('grande', 'salsiccia', 'funghi', 'cipolla')

end = time.perf_counter_ns()
print(f"\nTempo impiegato: {end - start}")
