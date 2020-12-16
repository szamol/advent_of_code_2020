import re
ranges = {}
my_ticket = ()
tickets = []

with open('input.txt', 'r') as f:

    line_to_tuple = lambda line: tuple([int(x) for x in line.split(',')])

    for line in f:
        if line == '\n':
            break
        else:
            name = re.findall(r'[a-z ]+(?=:)', line)[0]
            nums = re.findall(r'\d+', line.strip())
            ranges[name] = ((int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3])))

    next(f)
    my_ticket = line_to_tuple(f.readline())
    next(f)
    next(f)
    for line in f:
        tickets.append(line_to_tuple(line.strip()))

arr = []
for ticket in tickets:
    correct = True
    for number in ticket:
        for restrs in ranges.values():
            if restrs[0][0] <= number <= restrs[0][1] or restrs[1][0] <= number <= restrs[1][1]:
                break
        else:
            correct = False
            break
    if not correct:
        arr.append(ticket) 

tickets = [x for x in tickets if x not in arr]

orders = {k: set() for k in range(len(ranges))}

for ticket in tickets:
    for idx, number in enumerate(ticket):
        for name, restrs in ranges.items():
            if restrs[0][0] <= number <= restrs[0][1] or restrs[1][0] <= number <= restrs[1][1]:
                continue
            else:
                orders[idx].add(name)

attrs = list(ranges.keys())
orders = {x : y for x, y in sorted(orders.items(), key=lambda x : len(x[1]), reverse=True)}
idxs = []



for idx, incorrect in orders.items():
    for attr in attrs:
        if attr not in incorrect:
            print(idx, attr)
            if attr.startswith('departure'):
                idxs.append(idx)
            attrs.remove(attr)
            break
result = 1

for idx in idxs:
    result *= my_ticket[idx]
print(result)