def arabic_to_roman(n):
    roman_numbers = (
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100),
        ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),
        ("V", 5), ("IV", 4), ("I", 1))
    
    roman = ""
    for lettera, numero in roman_numbers:
        while n >= numero:
            roman += lettera
            n -= numero
    return roman


print(arabic_to_roman(2023))
print(arabic_to_roman(1996))
print(arabic_to_roman(2019))

for x in range(1, 13):
    print(f'{arabic_to_roman(x)}', end = '\t')