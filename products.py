import os


#  讀取檔案
def read_file(_):
    products = []
    with open(_, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products


#  讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        products.append([name, price])
    print(products)
    return products


#  印出紀錄
def print_products(products):
    for _ in products:
        print(_[0], '的價格是', _[1])


#  寫入檔案
def write_file(_, products):
    with open(_, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for _ in products:
            f.write(_[0] + ',' + str(_[1]) + '\n')


def main(_):
    if os.path.isfile(_):
        print('找到檔案了!')
        products = read_file(_)
    else:
        print('檔案不存在!')

    products = user_input(products)
    print_products(products)
    write_file(_, products)


main('products.csv')
