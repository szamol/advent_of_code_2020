instrs = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        instrs.append((line[0], int(line[1])))


def execute(instrs_list):
    rip = 0
    acc = 0
    instrs_done = []
    is_loop = False

    while not is_loop:
        try:
            curr_instr, curr_arg = instrs_list[rip]
        except IndexError:
            return acc
        if rip in instrs_done:
            return instrs_done
            
        instrs_done.append(rip)
        if curr_instr == 'acc':
            acc += curr_arg
            rip += 1
        elif curr_instr == 'jmp':
            rip += curr_arg
        else:
            rip += 1

instrs_done = execute(instrs)
to_check = [x for x in instrs_done if instrs[x][0] != 'acc']

for check in to_check:
    new_instrs = instrs.copy()
    change_instr, change_arg = new_instrs[check]
    if change_instr == 'nop':
        new_instrs[check] = ('jmp', change_arg)
    else:
        new_instrs[check] = ('nop', change_arg)

    result = execute(new_instrs)
    if type(result) is int:
        print(result)
