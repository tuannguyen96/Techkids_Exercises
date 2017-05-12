size = {
        'height' : 5,
        'width' : 4
        }

c = {
    'x' : 2,
    'y' : 1
    }

boxes = [
    {
        'x': 1,
        'y': 2
    },
    {
        'x': 2,
        'y': 2
    }
]

s_points = [
    {
    'x' : 3,
    'y' : 4
    },
    {'x': 3,
     'y': 3
     }
]

def position_in_list(points, x, y):
    for point in points:
        if point['x'] == x and point['y'] == y:
            return points.index(point)
    return None

def display_map(size, c, boxes, s_points):
    for y in range(size['height']):
        for x in range(size['width']):
            if x == c['x'] and y == c['y']:
                print('C ', end ='')
            elif position_in_list (boxes, x, y) is not None:
                print('B ', end = '')              
            elif position_in_list(s_points, x, y) is not None:
                print('S ', end = '')
            else:
                print('- ', end ='')
        print()

def in_map(size, point):
    return point['x'] >= 0 and point['x'] < size['width'] \
           and point['y'] >= 0 and point['y'] < size['height']

def move_point(point, dx, dy):
    return {
        'x' : point['x'] + dx,
        'y': point['y'] + dy
        }
def same_point(point1, point2):
    return point1['x'] == point2['x'] and point1['y'] == point2['y']

loop = True

while (loop):
    display_map(size,c,boxes,s_points)

    move = input('your move?').upper()
    print('Your pressed ',move)
    dx = 0
    dy = 0

    if move == 'D':
            dx = 1
    elif move == 'A':
            dx = -1
    elif move == 'W':
            dy = -1
    elif move  == 'S':
            dy = 1
            
    c_next = move_point(c, dx, dy)

    if in_map(size, c_next):
        box_index = position_in_list(boxes, c_next['x'], c_next['y'])
        if box_index is not None:
            box_next = move_point(boxes[box_index], dx, dy)
            box2_index = position_in_list(boxes, box_next['x'], box_next['y'])
            if box2_index is not None:
                print('You cant push 2 boxes')
            else:
                if in_map(size, box_next):
                    boxes[box_index] = box_next
                    c = c_next
        else:
            c = c_next
    check_box = position_in_list(s_points, box_next['x'], box_next['y'])
    if check_box is None:
        boxes.remove(check_box)
        

print('Tro choi ket thuc')        
