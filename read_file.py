with open('file.txt', 'r') as file:
    content = file.read()

if 'ciao' in content:
    print('found')