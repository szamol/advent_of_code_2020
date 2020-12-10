
elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(int(line.strip()))
        
elems.append(0)
elems.append(max(elems) + 3)
elems.sort()

ones = 0
threes = 0

for idx in range(len(elems) - 1):
    if elems[idx] + 1 == elems[idx + 1]:
        ones += 1
    elif elems[idx] + 3 == elems[idx + 1]:
        threes += 1

print(ones * threes)

    