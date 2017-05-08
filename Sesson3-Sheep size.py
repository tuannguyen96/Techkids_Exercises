sheep_size = [5, 7, 300, 90, 24, 50, 75]
Total_month = input("How many months do you want to feed the sheeps?")
month = 0


## Calculate sheep size after every month
for i in range(int(Total_month)):
    month = month + 1
    print("MONTH", month)
    
    print("Hello, my name is Tuan, here is my flock is", sheep_size)
    a = max(sheep_size)
    
    print("Now my biggest sheep has size", a, "let's shear it")
    position = sheep_size.index(a)
    sheep_size[position] = 8

    print(sheep_size)

    for i in range (6):
        sheep_size[i] = int(sheep_size[i]) + 50

    print("One month passed, now here is my flock:", sheep_size)


## Calculate money
Total_size = 0
for a in range (len(sheep_size)):
    Total_size = Total_size + int(sheep_size[i])

money = Total_size * 2
print("My flock has size in total:", Total_size)
print("I would get", money, "$")
                  
