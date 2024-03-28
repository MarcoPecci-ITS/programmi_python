#print(ord('a'))  # Da lettera a unicode
#print(chr(97))  # Da unicode a lettera

def encrypt(frase_da_cifrare, chiave_segreta):
    alfabeto_minuscolo = list('abcdefghijklmnopqrstuvwxyz')
    alfabeto_maiuscolo = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    messaggio_cifrato = []
    
    for lettera in frase_da_cifrare:
        if lettera in alfabeto_minuscolo:
            if (ord(lettera) + chiave_segreta) > 122:
                messaggio_cifrato.append(chr(ord(lettera) + chiave_segreta - 26))
            elif (ord(lettera) + chiave_segreta) < 97:
                messaggio_cifrato.append(chr(ord(lettera) + chiave_segreta + 26))
            else:
                messaggio_cifrato.append(chr(ord(lettera) + chiave_segreta))

        elif lettera in alfabeto_maiuscolo:
            if (ord(lettera) + chiave_segreta) > 90:
                messaggio_cifrato.append(chr(ord(lettera) + chiave_segreta - 26))
            elif (ord(lettera) + chiave_segreta) < 65:
                messaggio_cifrato.append(chr(ord(lettera) + chiave_segreta + 26))
            else:
                messaggio_cifrato.append(chr(ord(lettera) + chiave_segreta))

        else:
            messaggio_cifrato.append(lettera)
    
    return messaggio_cifrato


def decrypt(frase_cifrata, chiave_segreta):
    chiave_segreta = -chiave_segreta
    messaggio_decifrato = encrypt(frase_cifrata, chiave_segreta)
    return messaggio_decifrato