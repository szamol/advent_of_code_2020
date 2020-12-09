bags = {}

with open('input.txt', 'r') as f:
    for line in f:
        desc_list = line.strip().replace('bags', '').replace('bag', '')[:-1].split('contain')
        children_desc = desc_list[1].split(',')
        children = []
        if children_desc[0].replace(' ', '') != 'noother':
            for desc in children_desc:
                child = desc.strip().split(' ', 1)
                children.append((int(child[0]), child[1].replace(' ', '')))
        bags[desc_list[0].replace(' ', '')] = children

def get_total(name):
    curr = bags[name]
    if len(curr) == 0:
        return 0
    else:
        sum = 0
        for child in curr:
            sum = sum + child[0] + child[0] * get_total(child[1])
        return sum

print(get_total('shinygold'))
