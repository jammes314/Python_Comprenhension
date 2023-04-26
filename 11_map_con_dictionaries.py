items = [
{'product' : 'camisa',

'price' : 100,

},
{
    'product' : 'pantalon',
    'price' : 200

},
{
'product' : 'corbata',
'price' : 300
}
]

prices=list(map(lambda item: item['price'], items))

print(items)
print(prices)

def add_taxes(item):
    item['taxes'] = item['price']* 0.19
    return item
new_items = list(map(add_taxes, items))
print(new_items)
