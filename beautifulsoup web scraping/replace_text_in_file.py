with open('test.txt', 'r') as file:
    
    testo = file.read()
    
    for line in testo:
        testo = testo.replace('h ', 'h')
        #  \t tab
        

with open('test.txt', 'w') as file:
    file.write(testo)
