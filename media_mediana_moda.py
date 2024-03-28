import random

wages_first_group = [1000, 1100, 1200, 1300, 1400, 1500, 1500, 1600, 1700, 1800, 1900, 2000]
wages_second_group = [0, 0, 0, 1300, 1450, 1600, 1720, 1850, 6300, 5000]


def average(list):
    media = sum(list)/len(list)
    return round(media, 3)


def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[len(list)//2] + list[len(list)//2 - 1]) / 2
    else:
        return list[len(list)//2]


def mode(list):
    return max(list, key = list.count)


print(f'''Stipendi gruppo 1: {wages_first_group}\nMedia: {average(wages_first_group)}
Mediana: {median(wages_first_group)}\nModa: {mode(wages_first_group)}''')
print()
print(f'''Stipendi gruppo 2: {wages_second_group}\nMedia: {average(wages_second_group)}
Mediana: {median(wages_second_group)}\nModa: {mode(wages_second_group)}''')