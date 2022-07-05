products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

for _ in products:
    print(_[0], '的價格是', _[1])

with open('products.csv', 'w') as f:
    for _ in products:
        f.write(_[0] + ',' + _[1] + '\n')
