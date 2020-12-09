instrs = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        instrs.append((line[0], int(line[1])))

rip = 0
acc = 0

instrs_done = []

while True:
    curr_instr, curr_arg = instrs[rip]
    if rip in instrs_done:
        print('Last value before endless loop is {}'.format(acc))
        break
    instrs_done.append(rip)
    
    if curr_instr == 'acc':
        acc += curr_arg
        rip += 1
    elif curr_instr == 'jmp':
        rip += curr_arg
    else:
        rip += 1