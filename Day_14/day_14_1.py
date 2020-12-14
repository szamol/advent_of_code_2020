import re

memory = {}

def get_new_memory_value(mask, value):
    result = ''
    value = str(bin(int(value)))[2:].rjust(len(mask), '0')
    for c in zip(mask, value):
        if c[0] == 'X':
            result += c[1]
        else:
            result += c[0]
    return int(result, 2)

with open('input.txt', 'r') as f:
    mask = ''
    for line in f:
        if line == '\n':
            break
        else:
            if line.startswith('mask'):
                mask = line.replace('mask = ', '').strip()
            else:
                addr, value = line.split(' = ')
                addr = ''.join(filter(str.isdigit, addr.strip()))
                memory[addr] = get_new_memory_value(mask, value)

print(sum(memory.values()))
