elems = []

with open('input.txt', 'r') as f:
    answers = []
    for line in f:
        if line != '\n':
            answers.append(line.strip())
        else:
            elems.append(answers)
            answers = []
            
total = 0
for elem in elems:
    cnt = 0
    ppl_num = len(elem)
    combined_answers = ''.join(elem)
    for letter in set(combined_answers):
        if combined_answers.count(letter) == ppl_num:
            cnt += 1
    total += cnt

print(total)