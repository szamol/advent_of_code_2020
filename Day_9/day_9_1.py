
elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(int(line.strip()))

for idx in range(25, len(elems)):
    curr = elems[idx]

    for num1 in range(idx - 25, idx):
        found = False
        for num2 in range(num1, idx):
            if elems[num1] + elems[num2] == curr:
                found = True
        if found:
            break
    if not found:
        print("not found for {}".format(curr))
        break

    