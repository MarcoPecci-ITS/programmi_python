import os
clear = lambda: os.system("cls")

def cifrario_di_cesare(testo, chiave: int, scelta):
    """
    Cifra o decifra il testo utilizzando il cifrario di Cesare.
    :param testo: Il testo da cifrare o decifrare.
    :param chiave: Il numero di posizioni di spostamento per la cifratura (positivo per cifrare, negativo per decifrare).
    :return: Il testo cifrato o decifrato.
    """
    # per cifratura:
    numero_lettere = ord("z") - ord("a")

    # per decifratura:
    if scelta == 'd':
        numero_lettere = numero_lettere*(-1)

    testo = list(testo)
    testo_finale = []

    for carattere in testo:
        if not carattere.isalpha():
            testo_finale.append(carattere)
            continue

        if carattere.isupper():
            if ord(carattere) + chiave <= ord("Z"):
                testo_finale.append(chr(ord(carattere) + chiave))
            else:
                testo_finale.append(chr(ord(carattere) + chiave + numero_lettere))
            continue
        else:
            if ord(carattere) + chiave <= ord("z"):
                testo_finale.append(chr(ord(carattere) + chiave))
            else:
                testo_finale.append(chr(ord(carattere) + chiave - numero_lettere))
            continue

    return "".join(testo_finale)


def cifra_file(input_file, output_file, chiave, scelta):
    # param chiave: Il numero di posizioni di spostamento per la cifratura.
    try:
        with open(input_file, 'r') as file_in:
            testo_originale = file_in.read()
            testo_cifrato = cifrario_di_cesare(testo_originale, chiave, scelta)
            with open(output_file, 'w') as file_out:
                file_out.write(testo_cifrato)
        print(f"File cifrato salvato in {output_file}")
    except FileNotFoundError:
        print("File non trovato.")


def main():
    while True:
        clear()
        print("-- (exit) per uscire --")
        scelta = (input("Vuoi cifrare(c) o decifrare(d)? ")).lower()
        
        if scelta == "exit":
            break
        elif scelta == "c":
            input_file_path = "C:/Users/marco.pecci/Documents/programmi_python/cifrario_Cesare/testo_originale.txt"
            output_file_path = "C:/Users/marco.pecci/Documents/programmi_python/cifrario_Cesare/testo_cifrato.txt"
        elif scelta == "d":
            input_file_path = "C:/Users/marco.pecci/Documents/programmi_python/cifrario_Cesare/testo_cifrato.txt"
            output_file_path = "C:/Users/marco.pecci/Documents/programmi_python/cifrario_Cesare/testo_decifrato.txt"

        chiave_di_cifratura: int = int(input('Inserire chiave di cifratura(pos)/decifratura(neg): '))
        cifra_file(input_file_path, output_file_path, chiave_di_cifratura, scelta)


main()