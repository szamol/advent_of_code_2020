with open('input.txt', 'r') as f:
    spoken = list(map(int, f.readline().strip().split(',')))

person = len(spoken)

while person != 2020:
    last = spoken[-1]
    if spoken.count(last) < 2:
        spoken.append(0)
    else:
        tmp = [idx for idx, x in enumerate(spoken) if x == last][::-1]
        distance = tmp[0] - tmp[1]
        spoken.append(distance)
    
    person += 1

print(spoken[-1])