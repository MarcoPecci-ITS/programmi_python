import random
import string
import sys


def crea_codice_prodotto(length: int, segments: int) -> str:
    segment_length = length // segments

    codice = ""
    for _ in range(length):
        lettera = random.choice(string.ascii_uppercase)
        numero = str(random.randint(0, 9))
        codice += random.choice((lettera, numero))
    codice = [(codice[i:i + segment_length]) for i in range(0, len(codice), segment_length)]

    return "-".join(codice)


def extract_arguments(arg_list: list[str], default_n=0, default_l=0, default_s=0) \
        -> tuple[int, int, int]:
    number_of_codes, code_length, segments = default_n, default_l, default_s
    for i, argument in enumerate(arg_list):
        match argument:
            case "-n":
                number_of_codes = int(arg_list[i + 1])
            case "-l":
                code_length = int(arg_list[i + 1])
            case "-s":
                segments = int(arg_list[i + 1])

    return number_of_codes, code_length, segments


def get_user_input() -> tuple[int, int, int]:
    # first check for command line arguments
    argv: list[str] = sys.argv[1:]
    number_of_codes, code_length, segments = extract_arguments(argv)  # number_of_codes, code_length, segments

    # if there are no command line arguments, ask for user input
    while not all((number_of_codes, code_length, segments)):
        print(f"-n Numero di codici da generare: {number_of_codes}\n"
              f"-l Lunghezza del codice: {code_length}\n"
              f"-s Numero di segmenti: {segments}")
        user_input = input("Inserire i dati mancanti nella forma -variabile numero (ad esempio -l 20): ")
        number_of_codes, code_length, segments = extract_arguments(
                                                    user_input.split(), number_of_codes, code_length,
                                                    segments)

    return number_of_codes, code_length, segments


def stampa_codici() -> None:
    numero_codici, lunghezza_codice, segmenti = get_user_input()

    if lunghezza_codice % segmenti != 0:
        print(f"{lunghezza_codice} non è divisibile per {segmenti}")
        return

    for _ in range(int(numero_codici)):
        print(crea_codice_prodotto(lunghezza_codice, segmenti))


stampa_codici()
