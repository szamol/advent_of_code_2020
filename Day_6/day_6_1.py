elems = []

with open('input.txt', 'r') as f:
    answers = ""
    for line in f:
        if line != '\n':
            answers += line.strip()
        else:
            elems.append(answers)
            answers = ""

questions = 0
for elem in elems:
    questions += len(set(elem))

print(questions)