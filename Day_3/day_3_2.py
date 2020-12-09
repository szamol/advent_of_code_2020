elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(line.strip())

def count_trees(x_diff, y_diff):
    trees = 0
    x = y = 0
    chunk_width = len(elems[0])
    while y < len(elems):
        if elems[y][x%chunk_width] == '#':
            trees += 1
        x += x_diff
        y += y_diff
    return trees

styles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1

for style in styles:
    result *= count_trees(*style)

print(result)