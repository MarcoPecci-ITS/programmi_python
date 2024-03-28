def discounted_price(price, discount):
    new_price = round(price - (price * discount), 2)
    assert price > new_price > 0 
    return new_price

print(f'{discounted_price(3, 0.11)}$')