#  讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])

#  讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name, price])
print(products)

#  印出紀錄
for _ in products:
    print(_[0], '的價格是', _[1])

#  寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for _ in products:
        f.write(_[0] + ',' + _[1] + '\n')
