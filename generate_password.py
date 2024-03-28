import random
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$', '%', '!', '?']

def generate_password(how_long):
    random_password = ''
    for x in range(how_long):
        random_password += characters[random.randint(0, 41)]
    print(random_password)
    

while True:
    generate_password(16)
    break