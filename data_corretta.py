def correct_date(day, month, year):
    if not (1 <= day <= 31) or not (1 <= month <= 12):
        return False
    if month in (4, 6, 9, 11) and day == 31:
        return False
    if month == 2 and day == 29 and is_leap_year(year):
        return True
    if month == 2 and day > 28:
        return False
    
    return True


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    data = input('Inserisci una data GG/MM/AAAA e ti dirò se esiste o no: ').split('/')
    giorno, mese, anno = data

    risposta = correct_date(int(giorno), int(mese), int(anno))
    print(risposta)