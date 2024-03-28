# USER AND PASSWORD GENERATOR
import random
number_of_users = 2102
utenti = {}


def new_user():
    global number_of_users
    
    name = 'user_' + str(number_of_users + 1)
    password = random.randint(100_000_000, 999_999_999)
    
    utenti[name] = password
    number_of_users += 1
    

for _ in range(5):
    new_user()

print(utenti)