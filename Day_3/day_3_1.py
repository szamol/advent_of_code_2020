elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(line.strip())

trees = 0
x = y = 0
chunk_width = len(elems[0])
while y != len(elems):
    if elems[y][x%chunk_width] == '#':
        trees += 1
    x += 3
    y += 1

print(trees)