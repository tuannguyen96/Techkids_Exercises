##Exercise 3

groceries = {
    'stock': {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
        },
    'prices': {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }
}

print(groceries)

total = 0

food = ['banana', 'apple', 'orange']

def compute_bill(food):
    for key, value in groceries[food].items():
        print(groceries)

compute_bill
