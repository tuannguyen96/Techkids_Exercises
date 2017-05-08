##Exercise 1

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"]=["seashell", "strange berry", "lint"]

inventory['backpack'].sort()
print (inventory['backpack'])

inventory['backpack'].remove('dagger')
print (inventory['backpack'])

inventory['gold']=500+50
print(inventory['gold'])
