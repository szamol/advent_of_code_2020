elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(int(line.strip()))

elems.append(0)
elems.append(max(elems) + 3)
elems.sort()

ways = [1] * (elems[-1] + 1)
for elem in elems[1:]:
    ways[elem] = sum(ways[num] for num in range(elem - 3, elem) if num in elems)

print(ways[-1])








    


