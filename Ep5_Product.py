product = {'Pencil' : {'price':50,'color':'red'},
           'Eraser': {'price':10,'color':'white'},
           'Pencolor':{'price':100,'color':'orange'}}

while True:
    print('\n----Please insert the detail----')
    p = input('Product name: ')
    if p in product:
        q = int(input('Quantity : '))
        print('----------\n')
        print(f'Product : {p}\nPrice : {product[p]['price']} \nColor : {product[p]['color']}')
        print(f'Total quantity : {q} units\nTotal price : {product[p]['price']*q}')
    else:
        print('Sorry, We do not have this item')
