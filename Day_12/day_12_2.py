from math import sin, cos, radians
elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append((line[0], line.strip()[1:]))

w_x = 10
w_y = -1
s_x = 0
s_y = 0

for elem in elems:
    action, value = elem
    value = int(value)

    if action == 'F':
        s_x += value * w_x
        s_y += value * w_y
    elif action == 'N':
        w_y -= value
    elif action == 'S':
        w_y += value
    elif action == 'W':
        w_x -= value
    elif action == 'E':
        w_x += value

    elif action in ['L', 'R']:
        if action == 'L':
            value *= -1
        value = radians(value)
        x = int(cos(value)) * w_x - int(sin(value)) * w_y
        y = int(sin(value)) * w_x + int(cos(value)) * w_y
        w_x, w_y = x, y

print(abs(s_x) + abs(s_y))