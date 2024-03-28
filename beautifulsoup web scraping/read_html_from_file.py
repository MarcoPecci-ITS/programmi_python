from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')
'''    
print(doc.prettify())

tag = doc.title  # It only shows the first title if there are more than one
print(tag)

tag.string = 'Titolo modificato'  # Modificare qualcosa
print(tag)

tag2 = doc.find('a')  # Trova il primo
print(tag2)
tag3 = doc.find_all('a')  # Trova tutti
print(tag3)
'''
tags = doc.find_all('p')[0]  # find b nested inside p
print(tags.find_all('b'))