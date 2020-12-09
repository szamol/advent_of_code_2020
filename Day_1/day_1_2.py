
elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(int(line.strip()))

for x in range(len(elems)):
    for y in range(x, len(elems)):
        for z in range(y, len(elems)):
            if elems[x] + elems[y] + elems[z] == 2020:
                print(elems[x] * elems[y] * elems[z])