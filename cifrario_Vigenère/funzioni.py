def cypher(lettera, codice):
    if ord(lettera) + codice > 122:
        new = chr(ord(lettera) + codice -26)
        return new
    elif ord(lettera) + codice < 97:
        new = chr(ord(lettera) + codice +26)
        return new
    else:
        new = chr(ord(lettera) + codice)
        return new

def decypher(lettera, codice):
    codice = -codice
    new = cypher(lettera, codice)
    return new