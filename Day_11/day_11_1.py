
state = []

with open('input.txt', 'r') as f:
    for line in f:
        state.append(list(line.strip()))

width = len(state[0])
height = len(state)

adj_seats = lambda sub: sum([x.count('#') for x in sub]) 
get_min_range = lambda num: num - 1 if num - 1 >= 0 else 0
get_max_range = lambda num: num + 2 if num + 2 <= width else num + 1

while True:
    change = False
    new_state = [x[:] for x in state]

    for y in range(height):
        for x in range(width):
            curr = state[y][x]
            sub = [r[get_min_range(x):get_max_range(x)] for r in state[get_min_range(y):get_max_range(y)]]
            adj = adj_seats(sub)
            if curr == 'L' and adj == 0:
                new_state[y][x] = '#'
                change = True
            elif curr == '#' and adj - 1 >= 4:
                new_state[y][x] = 'L'
                change = True

    state = [x[:] for x in new_state]
    if not change:
        break

taken = sum([x.count('#') for x in state])
print(taken)
            