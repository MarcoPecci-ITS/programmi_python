from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.it/POCO-Pro-Smartphone-DotDisplay-Snapdragon/dp/B0BSFZF7DN/'

result = requests.get(url)
# print(result.text)

doc = BeautifulSoup(result.text, 'html.parser')
# print(doc.prettify())

prices = doc.find_all(string='€')

print(type(prices))

for item in prices:
    parent = item.parent
    print(parent)