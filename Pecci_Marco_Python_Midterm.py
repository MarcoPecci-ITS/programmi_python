# Marco Pecci - Verifica midterm Python

# 1) Gestione delle Risorse: classe con due attributi, nome e quantità
class Risorsa:
    def __init__(self, nome, quantity):
        self.nome = nome
        self.quantity = quantity

    def info_risorsa(self):
        print(f"Risorsa: {self.nome} -- Quantità: {self.quantity}")
# esempio:
# risorsa1 = Risorsa("Rame", 180)
# Risorsa.info_risorsa(risorsa1)


# 2) Ordinamento delle Risorse: funzione bubble sort
def ordina_risorse(risorse):
    for j in range(0, len(risorse)-1):
        for i in range(0, len(risorse)-1):
            if risorse[i].quantity > risorse[i + 1].quantity:
                risorse[i].quantity, risorse[i + 1].quantity = risorse[i + 1].quantity, risorse[i].quantity
    return risorse
#esempio:     
elenco_risorse = [Risorsa("Ferro", 100), Risorsa("Carbone", 70), Risorsa("Stagno", 150)]
# print(elenco_risorse)
print(ordina_risorse(elenco_risorse))


# 3) Ricerca Binaria Avanzata
def binary_search(lista, basso, alto, elemento_da_trovare):
 
    if alto >= basso:
        mezzo = (alto + basso) // 2
 
        if lista[mezzo] == elemento_da_trovare:
            return mezzo
        elif lista[mezzo] > elemento_da_trovare:
            return binary_search(lista, basso, mezzo - 1, elemento_da_trovare)
        else:
            return binary_search(lista, mezzo + 1, alto, elemento_da_trovare)
    else:
        return -1
# esempio (NON FUNZIONA):
# elenco_risorse = [("Ferro", 100), ("Carbone", 70), ("Stagno", 150)]
# print(binary_search(elenco_risorse, 0, len(elenco_risorse), "Ferro"))


# 4) Dizionario di settori del pianeta e funzione per visualizzarne gli elementi
settori = {"Energia" : ["pannelli_solari", "rame", "pale_eoliche"],
           "Alimentazione" : ["acqua", "frutta", "verdura"],
           "Estrazione" : ["silicio", "minerali", "ferro"]}

def visualizza_risorse_settore():
    print("Settori del Pianeta:\n- Energia\n- Alimentazione\n- Estrazione\n\nDi quale settore si desidera vedere le risorse? ", end="")
    settore_scelto = input()
    for elemento in settori[settore_scelto]:
        print(elemento, end="  ")
# esempio:
# visualizza_risorse_settore()
        

# 5) Ereditarietà: classe RisorsaSpeciale di tipo Risorsa, con attributo rarità
class RisorsaSpeciale(Risorsa):
    def __init__(self, nome, quantity, rarity):
        self.nome = nome
        self.quantity = quantity
        self.rarity = rarity

    def info_risorsa_speciale(self):
        print(f"Risorsa: {self.nome} -- Quantità: {self.quantity} -- Rarità: {self.rarity}")
# esempio:
# specialOne = RisorsaSpeciale("Diamanti", 10, "Alta")
# RisorsaSpeciale.info_risorsa_speciale(specialOne)