SCONTI = [0, 0.05, 0.1, 0.2, 0.25]
prezzo_libro = 8

ordini = [{"Book1": 0, "Book3": 2, "Book4": 5, "Book5": 1},
          {"Book1": 1, "Book2": 2, "Book3": 4, "Book4": 1, "Book5": 2},
          {"Book3": 1, "Book4": 1, "Book5": 1},
          {"Book1": 1, "Book2": 1, "Book3": 1, "Book4": 1, "Book5": 1},
          {"Book1": 2, "Book3": 1, "Book4": 1, "Book5": 1},
          {"Book3": 3, "Book4": 3, "Book5": 3},
          {}]


def update_list(order: list, minimum: int = 0):
    new_list = []
    for amount in order:
        if amount in (0, None, "") or amount == minimum:
            pass
        elif amount > minimum:
            new_list.append(amount - minimum)
        else:
            new_list.append(amount)
    return new_list


def calculate_price(order: list, sconti: list) -> tuple[int, int]:
    total_books, total_price = 0, 0

    while True:
        books_bought = 0
        if not order:
            return total_books, round(total_price, 2)

        min_amount = min(order)
        i = -1
        for item in order:
            if item >= min_amount:
                books_bought += min_amount
                i += 1

        total_price += books_bought * prezzo_libro * (1 - sconti[i])
        total_books += books_bought
        order = update_list(order, min_amount)
        print(f"libri comprati: {books_bought} sconto: {sconti[i]*100}% prezzo: {total_price}\n{order}")


for ordine in ordini:
    lista_ordine = [amount for amount in ordine.values() if amount not in (0, None, "")]
    print(lista_ordine)
    libri_comprati, prezzo = calculate_price(lista_ordine, SCONTI)

    print(f"Libri comprati: {libri_comprati}\t Spesa totale: {prezzo}€\n")
