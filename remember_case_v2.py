frase_iniziale = 'Frase con MAIUSCOLE e minuscole.'
frase_minuscola = frase_iniziale.lower()

posizione_maiuscole = [True if lettera.isupper() else False
                       for index, lettera in enumerate(frase_iniziale)]

frase_finale = (lettera.upper() if posizione_maiuscole[pos] else lettera
                for pos, lettera in enumerate(frase_minuscola))

print(f"1) {frase_iniziale}"
      f"\n2) {frase_minuscola}"
      f"\n3) {"".join(frase_finale)}")
