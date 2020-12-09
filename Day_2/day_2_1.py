elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(line.strip())

valid = 0

for elem in elems:
    arr = elem.split()
    ranges = arr[0].split('-')
    if int(ranges[0]) <= arr[2].count(arr[1].replace(':', '')) <= int(ranges[1]):
        valid += 1

print(valid)