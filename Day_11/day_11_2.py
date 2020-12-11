
state = []

with open('input.txt', 'r') as f:
    for line in f:
        state.append(list(line.strip()))

width = len(state[0])
height = len(state)

def get_adj_seats(y, x):

    directions = []

    directions.append(state[y][:x][::-1])
    directions.append(state[y][x + 1:])
    directions.append([row[x] for row in state[:y]][::-1])
    directions.append([row[x] for row in state[y + 1:]])

    diag1 = [] # upper \
    b, a = y, x
    while a >= 0 and b >= 0:
        if a != x and b != y:
            diag1.append(state[b][a])
        a -= 1
        b -= 1
        
    directions.append(diag1)

    diag2 = [] # upper /
    b, a = y, x
    while b >= 0 and a < width:
        if a != x and b != y:
            diag2.append(state[b][a])
        a += 1
        b -= 1
    directions.append(diag2)

    diag3 = [] # lower \
    b, a = y, x
    while b < height and a < width:
        if a != x and b != y:
            diag3.append(state[b][a])
        a += 1
        b += 1
    directions.append(diag3)


    diag4 = [] # lower /
    b, a = y, x
    while b < height and a >= 0:
        if a != x and b != y:
            diag4.append(state[b][a])
        a -= 1
        b += 1
    directions.append(diag4)

    adj_seats = 0
    for direction in directions:
        for seat in direction:
            if seat == 'L':
                break
            elif seat == '#':
                adj_seats += 1
                break
    
    return adj_seats

idx = 0
while True:
    change = False
    new_state = [x[:] for x in state]

    for y in range(height):
        for x in range(width):
            curr = state[y][x]
            if curr != '.':
                adj = get_adj_seats(y, x)
                if curr == 'L' and adj == 0:
                    new_state[y][x] = '#'
                    change = True
                elif curr == '#' and adj >= 5:
                    new_state[y][x] = 'L'
                    change = True

    state = [x[:] for x in new_state]
    if not change:
        break

taken = sum([x.count('#') for x in state])
print(taken)
            