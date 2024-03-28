def is_date_correct(day, month, year) -> bool:
    if (day < 1 or day > 31) or (month < 1 or month > 12):
        return False
    elif month in (4, 6, 9, 11) and day > 30 or month == 2 and day > 29:
        return False
    elif month == 2 and day == 29 and not is_leap(year):
        return False

    return True


def is_leap(year) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    print('Inserisci una data GG/MM/AAAA e ti dirò se esiste o no: ', end='')
    giorno, mese, anno = map(int, input().split('/'))
    print(is_date_correct(giorno, mese, anno))
