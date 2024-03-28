import random
lanci = []

for i in range(25):
    lanci.append(random.randint(0, 1))

print(lanci)

testa = lanci.count(0)
croce = lanci.count(1)
print(f'Testa: {testa}\nCroce: {croce}')