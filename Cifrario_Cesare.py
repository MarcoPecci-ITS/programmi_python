# cifra o decifra (a seconda del valore del parametro mode) una stringa di testo in base al valore della chiave
def cifra_decifra(message: str, key: int, mode: str) -> str:
    result = ""
    for char in message:
        if not char.isalpha():
            result += char  # se il carattere non è una lettera non fa nulla
            continue

        shift = key % 26  # per controllare che la chiave sia sempre compresa tra 0 e 25
        ascii_offset = 97 if char.islower() else 65

        if mode == 'cifra':
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        elif mode == 'decifra':
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
    return result


# fa un brute force di un testo cifrato provando tutte le 26 combinazioni possibili e restituisce una lista di stringhe
def brute_force(testo_da_decifrare: str) -> list[str]:
    lista_candidati = []
    for key in range(26):
        frase = cifra_decifra(testo_da_decifrare, key, "decifra")
        lista_candidati.append(frase)
    return lista_candidati


# restituisce un dizionario con le lettere del testo come chiavi e la percentuale di frequenza delle stesse come valori
def letter_frequency(testo: str) -> dict:
    numero_lettere = 0
    frequenze_lettere: dict = {}

    # conta quante volte compaiono le lettere nel testo
    for carattere in testo:
        if not carattere.isalpha():
            continue  # se il carattere non è una lettera non fa nulla

        carattere = carattere.lower()  # tutte le lettere sono convertite in minuscolo
        if carattere in frequenze_lettere.keys():
            frequenze_lettere[carattere] += 1
        else:
            frequenze_lettere[carattere] = 1
        numero_lettere += 1
    
    # ordina le lettere in ordine alfabetico
    frequenze_lettere = dict(sorted(frequenze_lettere.items()))

    # divide il numero di apparizioni di una lettera per il numero di lettere totali, per trovare le percentuali di frequenza
    for key in frequenze_lettere.keys():
        frequenze_lettere[key] = frequenze_lettere[key]/numero_lettere

    return frequenze_lettere


''' confronta la frequenza delle lettere di un testo con quelle della lingua di riferimento, restituisce un valore float
    che rappresenta la somma delle differenze tra le frequenze di ogni lettera dei testi '''
def frequency_compare(frequenze_lettere_testo : dict, lingua_di_riferimento : dict) -> float:
    differenza_frequenze = []
    for lettera in lingua_di_riferimento:
        try:
            differenza_frequenze.append(abs(frequenze_lettere_testo[lettera] - lingua_di_riferimento[lettera]))
        except KeyError:
            differenza_frequenze.append(lingua_di_riferimento[lettera])
            
    return sum(differenza_frequenze)


# DIZIONARI DELLE FREQUENZE
english_frequencies = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
        'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
        'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
        'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
        'z': 0.00074}

italian_frequencies = {
        'a': 0.1175, 'b': 0.0092, 'c': 0.0450, 'd': 0.0373, 'e': 0.1179,
        'f': 0.0095, 'g': 0.0164, 'h': 0.0154, 'i': 0.1128, 'j': 0.0000,
        'k': 0.0000, 'l': 0.0651, 'm': 0.0251, 'n': 0.0688, 'o': 0.0983,
        'p': 0.0305, 'q': 0.0051, 'r': 0.0637, 's': 0.0498, 't': 0.0562,
        'u': 0.0301, 'v': 0.0210, 'w': 0.0000, 'x': 0.0000, 'y': 0.0000,
        'z': 0.0049}


TESTO_IN_CHIARO : str = "Messaggio segreto da trovare con molte parole in Italiano per l'analisi delle frequenze."
CHIAVE : int = 14
messaggio_criptato : str = cifra_decifra(TESTO_IN_CHIARO, CHIAVE, "cifra")


''' dato un messaggio cifrato e una lingua di riferimento fa un brute force del messaggio e restituisce i 26 candidati,
    ordinandoli da quello più probabile a quello meno probabile in base all'analisi delle frequenze ''' 
def main(messaggio_da_decifrare: str, lingua_di_riferimento: dict) -> None:
    possibili_candidati: list[str] = brute_force(messaggio_da_decifrare)
    candidati_in_ordine = []  # lista di tuple (punteggio frequenze, frase)

    for frase in possibili_candidati:
        frequenze_lettere_frase = letter_frequency(frase)
        ''' il punteggio qui sotto non è una percentuale ma un numero che indica quanto la frequenza delle lettere
            sia vicina alla lingua di riferimento (numero più basso --> più vicino) '''
        punteggio = round(frequency_compare(frequenze_lettere_frase, lingua_di_riferimento), 3)
        candidati_in_ordine.append((punteggio, frase))

    candidati_in_ordine = sorted(candidati_in_ordine)

    print("\nEcco un'elenco di possibili candidati, in ordine dal più al meno probabile:\n")
    for indice, candidato in enumerate(candidati_in_ordine, 1):
        print(f"{indice})  {candidato[1]}\t({candidato[0]})")


main(messaggio_criptato, italian_frequencies)