import re
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
        match = re.match(r'^([0-9]+)(cm|in)$', elem['hgt'])
        if match:
            val, unit = match.groups()
            if (
                1920 <= int(elem['byr']) <= 2002 and # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                2010 <= int(elem['iyr']) <= 2020 and # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                2020 <= int(elem['eyr']) <= 2030 and # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                (unit == 'cm' and 150 <= int(val) <= 193 or # If cm, the number must be at least 150 and at most 193
                unit == 'in' and 59 <= int(val) <= 76) and # If in, the number must be at least 59 and at most 76.
                re.match(r'^#[0-9a-f]{6}$', elem['hcl']) and #a # followed by exactly six characters 0-9 or a-f.
                elem['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and # exactly one of: amb blu brn gry grn hzl oth.
                re.match(r'^[0-9]{9}$', elem['pid']) # a nine-digit number, including leading zeroes.
            ):
                valid += 1
    
print(valid)
