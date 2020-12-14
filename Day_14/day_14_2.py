from itertools import product

memory = {}

def get_addrs(mask, addr):
    addrs = []
    result = ''
    addr = str(bin(int(addr)))[2:].rjust(len(mask), '0')
    for c in zip(mask, addr):
        if c[0] == '1':
            result += '1'
        elif c[0] == '0':
            result += c[1]
        else:
            result += 'X'

    xs = result.count('X')
    gen = product('01', repeat=xs)

    for v in gen:
        new_addr = result
        for idx in range(xs):
            new_addr = new_addr.replace('X', v[idx], 1)
        addrs.append(new_addr)
    return addrs

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
                for addr in get_addrs(mask, addr):
                    memory[addr] = int(value)

print(sum(memory.values()))
