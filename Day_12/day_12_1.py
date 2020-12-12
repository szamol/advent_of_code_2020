
elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append((line[0], line.strip()[1:]))

directions = ['E', 'S', 'W', 'N']

facing = 'E'
x = 0
y = 0

for elem in elems:
    action, value = elem
    value = int(value)

    if action == 'F':
        action = facing

    if action == 'N':
        y -= value
    elif action == 'S':
        y += value
    elif action == 'W':
        x -= value
    elif action == 'E':
        x += value

    elif action in ['L', 'R']:
        value = value // 90
        if action == 'L':
            value *= -1
        idx = directions.index(facing)
        facing = directions[(value + idx) % 4]

print(abs(x) + abs(y))