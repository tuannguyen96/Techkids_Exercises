##Exercise 2

fruit= {
    'banana': { 'prices' : 4,
                'stock' : 6},
    'apple' : { 'prices' : 2,
                'stock'  :0},
    'orange' : { 'prices' : 1.5,
                 'stock' : 32},
    'pear' : { 'prices' : 3,
               'stock' : 15}

}

print(fruit)

for key, value in fruit.items():
    print (key)
    print('price:', value['prices'])

##Countmoney

total = 0
    
for key, value in fruit.items():
    total = total + int(value['prices']) * int(value['stock'])

print(total,'$')
