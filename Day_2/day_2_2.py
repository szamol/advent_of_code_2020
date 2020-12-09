elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(line.strip())

valid = 0

for elem in elems:
    arr = elem.split()
    idxs = arr[0].split('-')
    letter = arr[1].replace(':', '')
    i1 = arr[2][int(idxs[0]) - 1]
    i2 = arr[2][int(idxs[1]) - 1]
    if  i1 == letter and not i2 == letter or not i1 == letter and i2 == letter:
        valid += 1

print(valid)