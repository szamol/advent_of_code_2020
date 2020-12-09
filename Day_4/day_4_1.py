elems = []

req_attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('input.txt', 'r') as f:
    line_dict = {}
    for line in f:
        if line != '\n':
            for attrs in line.split():
                pair = attrs.split(':')
                line_dict[pair[0]] = pair[1]
        else:
            elems.append(line_dict)
            line_dict = {}

valid = 0
for elem in elems:
    if all(attr in elem for attr in req_attrs):
        valid += 1
    
print(valid)
