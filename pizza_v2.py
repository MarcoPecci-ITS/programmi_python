import time
base_price = 5


def make_pizza(size: str, *toppings: str) -> None:
    price = base_price + len(toppings)
    price += 1.5 if size == 'grande' else 0

    show_toppings = f"Pizza {size} con {", ".join(toppings)}"

    print(show_toppings + f"{price}€".rjust(70 - len(show_toppings), "_"))


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
