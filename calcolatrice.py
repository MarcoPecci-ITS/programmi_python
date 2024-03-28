def add(*args):
    risultato = 0
    for numero in args:
        risultato += numero
    return risultato


def subtract(*args):
    risultato = args[0]
    for numero in args[1:]:
        risultato -= numero    
    return risultato


def multiply(*args):
    risultato = 1
    for numero in args:
        risultato *= numero    
    return risultato


def divide(*args):
    risultato = args[0]
    for numero in args[1:]:
        risultato /= numero    
    return risultato


print('---CALCOLATRICE---')
while True:
    user_instruction = input("Inserire un'operazione: ")

    if '+' in user_instruction:
        print(add(*[int(n) for n in user_instruction.split('+')]))
    elif '-' in user_instruction:
        print(subtract(*[int(n) for n in user_instruction.split('-')]))
    elif '*' in user_instruction:
        print(multiply(*[int(n) for n in user_instruction.split('*')]))
    elif '/' in user_instruction:
        print(divide(*[int(n) for n in user_instruction.split('/')]))