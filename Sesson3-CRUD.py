our_items = ["T-Shirt", "Sweater"]
name = input("Welcome to our shop, what do you want (C, R, U, D)")

if name == "C":
    our_items.append("Jeans")
    print(our_items)
 
elif name == "R":
    print(our_items)
    
elif name == "U":
    position1 = int(input("Update position?"))
    new_item = input("New item?")
    our_items.insert(position1, new_item)
    print(our_items)
          
elif name == "D":
    position_delete = int(input("Delete position?"))
    del our_items[position_delete]
    print(our_items)
