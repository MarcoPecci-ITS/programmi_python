class Pets:
    def __init__(self, name, age, species, color):
        self.name = name
        self.age = age
        self.species = species
        self.color = color

pet1 = Pets('Fido', 7, 'dog', 'black')
pet2 = Pets('Mr. Brown', 4, 'cat', 'brown')
pet3 = Pets('Bongo', 1, 'fish', 'red')

my_animals = [pet1, pet2, pet3]
for pet in my_animals:
    print(f'{pet.name} is a {pet.age} years old {pet.color} {pet.species}.')