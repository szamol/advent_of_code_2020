from math import ceil

def get_next_row_range(row_from, row_to, letter):
    if letter == 'F':
        return row_from, ceil((row_from + row_to - 1) / 2)
    else:
        return ceil((row_from + row_to) / 2), row_to

def get_next_col_range(col_from, col_to, letter):
    if letter == 'L':
        return col_from, ceil((col_from + col_to - 1) / 2)
    else:
        return ceil((col_from + col_to) / 2), col_to

elems = []

with open('input.txt', 'r') as f:
    for line in f:
        elems.append(line.strip())

max_seat_id = 0

for elem in elems:
    row_data = elem[:7]
    row_from = 0
    row_to = 127
    
    col_data = elem[7:]
    col_from = 0
    col_to = 7
    
    for letter in row_data:
        row_from, row_to = get_next_row_range(row_from, row_to, letter)
    
    for letter in col_data:
        col_from, col_to = get_next_col_range(col_from, col_to, letter)

    seat_id = row_from * 8 + col_from
    
    if max_seat_id < seat_id:
        max_seat_id = seat_id

print(max_seat_id)