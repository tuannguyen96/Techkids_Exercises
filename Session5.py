##box = {'row': '2', 'column' : 3}
##storage_point = {'row' : '2', 'column' : 4}
##your_point = {'row' : '2', 'column' : 1}
##
##
##n= input("which way do you wanna move")
##
##def moving(n):
##    if n == 'W':
##        if int(your_point['row']) > 1:
##            your_point['row'] = int(your_point['row']) -1
##        else:
##            your_point['row'] = '4'
##        
##    elif n == 'S':
##        if int(your_point['row']) < 4:
##            your_point['row'] = int(your_point['row']) +1
##        else:
##            your_point['row'] = '1'
##        
##    elif n == 'A':
##        if int(your_point['column']) < 4:
##            your_point['column'] = int(your_point['column']) +1
##        else:
##            your_point['column'] = '1'
##        
##    elif n == 'D':
##        if int(your_point['column']) > 1:
##            your_point['column'] = int(your_point['column']) -1
##        else:
##            your_point['column'] = '4'

size = {
        'height' : 5,
        'width' : 4
        }

c = {
    'x' : 2,
    'y' : 1
    }

b = {
    'x' : 1,
    'y' : 3
    }

s = {
    'x' : 1,
    'y' : 1
    }

def display_map(size, c, b, s):
    for y in range(size['height']):
        for x in range(size['width']):
            if x == c['x'] and y == c['y']:
                print('C ', end ='')
            elif x == b['x'] and y == b['y']:
                print('B ', end = '')              
            elif x == s['x'] and y == s['y']:
                print('S ', end = '')
            else:
                print('- ', end ='')
        print()

loop = True

while(loop):
    display_map(size, c, b, s) 
    move = input('Ban muon di chuyen huong nao?').upper()
    print('you pressed', move)

    if move == "D":
        if c['x'] == int(size['width']) -1:
            print('Ban khong duoc di ra khoi ban do')
            print('Vui long di lai')
        else:
            c['x'] +=1

        if b == c:
            if b['x'] == int(size['width']) -1:
                print('Ban khong duoc day hop ra khoi ban do')
                print('Vui long di lai')
                c['x'] -=1
            else:
                b['x'] +=1
    elif move == 'A':
        if c['x'] == 0:
            print('Ban khong duoc di ra khoi ban do')
            print('Vui long di lai')
        else:
            c['x'] -=1

        if b == c:
            if b['x'] == 0:
                print('Ban khong duoc day hop khoi ban do')
                print('Vui long di lai')
                c['x'] +=1
            else:
                b['x'] -=1
                
    elif move == 'W':
        if c['y'] == 0:
            print('Ban khong duoc di ra khoi ban do')
            print('Vui long di lai')
        else:
            c['y'] -=1

        if b == c:
            if b['y'] == 0:
                print('Ban khong duoc day hop ra khoi ban do')
                print('Vui long di lai')
                c['y'] +=1
            else:
                b['y'] -=1
            
    elif move == 'S':
        if c['y'] == int(size['height']) -1:
            print('Ban khong duoc di ra khoi ban do')
            print('Vui long di lai')
        else:
            c['y'] +=1

        if b == c:
            if b['y'] == int(size['height']) -1:
                print('Ban khong duoc day hop ra khoi ban do')
                print('Vui long di lai')
                c['y'] -=1
            else:
                b['y'] +=1
                
       
    else:
        print('Hay dung cac phim A, S, D, W de di chuyen')
        print('Xin moi nhap lai')


    if b == s:
        print ('You won')
        loop = False
        sprint('Tro choi ket thuc')

