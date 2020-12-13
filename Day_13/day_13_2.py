elems = []

with open('input.txt', 'r') as f:
    f.readline()
    for offset, loop in enumerate(f.readline().split(',')):
        if loop != 'x':
            elems.append((int(loop), offset))

prod = 1
for loop, _ in elems:
    prod *= loop

total = 0

for loop, offset in elems:
    p = prod // loop
    total += -offset * pow(p, -1, loop) * p

print(total % prod)



