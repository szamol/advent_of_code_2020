import re
ranges = []
my_ticket = ()
tickets = []

with open('input.txt', 'r') as f:

    line_to_tuple = lambda line: tuple([int(x) for x in line.split(',')])

    for line in f:
        if line == '\n':
            break
        else:
            nums = re.findall(r'\d+', line.strip())
            ranges.append([(int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3]))])

    next(f)
    my_ticket = line_to_tuple(f.readline())
    next(f)
    next(f)
    for line in f:
        tickets.append(line_to_tuple(line.strip()))


errs = 0

for ticket in tickets:
    for number in ticket:
        correct = False
        for restrs in ranges:
            if restrs[0][0] <= number <= restrs[0][1] or restrs[1][0] <= number <= restrs[1][1]:
                correct = True
                break
        if not correct:
            errs += number
print(errs)     

