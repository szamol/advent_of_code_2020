bags = []

with open('input.txt', 'r') as f:
    for line in f:
        desc_list = line.strip().replace('bags', '').replace('bag', '')[:-1].split('contain')
        children = ''.join(l for l in desc_list[1] if not l.isdigit() and not l.isspace()).split(',')
        bags.append((desc_list[0].replace(' ', ''), children))


to_check = {'shinygold'}
gold_containers = set()

while len(to_check) != 0:
    new_checks = set()
    for bag in bags:
        for check in to_check:
            if check in bag[1]:
                gold_containers.add(bag[0])
                new_checks.add(bag[0])
    to_check = new_checks

print(len(gold_containers))
    

