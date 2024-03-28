def roman_to_arabic(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
            arabic += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
        else:
            arabic += roman_dict[roman[i]]
    return arabic

print(roman_to_arabic('MMXXIII'))
print(roman_to_arabic('MCMXCVI'))
print(roman_to_arabic('MMXIX'))