spoken = {}
with open('input.txt', 'r') as f:
    for idx, line in enumerate(f.readline().strip().split(',')):
        spoken[int(line)] = idx

person = len(spoken)

last = 0
while person != 29999999:
    if last in spoken:
        spoken[last], last = person, person - spoken[last]
    else:
        spoken[last], last = person, 0
    
    person += 1

print(last)