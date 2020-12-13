earliest = int()
loops = []

with open('input.txt', 'r') as f:
    earliest = int(f.readline().strip())
    for loop in f.readline().split(','):
        if loop != 'x':
            loops.append(int(loop))

possibilities = []

for loop in loops:
    rounds = earliest // loop
    if earliest % loop != 0:
        rounds += 1
    possibilities.append(rounds * loop)

departure = min(possibilities)
loop = loops[possibilities.index(departure)]

print((departure - earliest) * loop)