def unique_digits():
    return [i for i in range(1000, 10000) if len(set(str(i))) == len(str(i))]

print(unique_digits())

# il numero viene convertito in un set, per esempio la stringa '1233' diventa
# ('1', '2', '3'), siccome la lunghezza del set è diversa da quella della
# stringa il numero ha almeno una cifra che si ripete