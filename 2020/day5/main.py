import math

data = [line.strip() for line in open("input/input.in")]
seat_ids = []
seats = []
seats.append([])
seats.append([])
seats.append([])
seats.append([])
seats.append([])
seats.append([])
seats.append([])
seats.append([])
my_seat = 0
for line in data:
    low_row = 0
    high_row = 127
    low_c = 0
    high_c = 7
    for index, char in enumerate(line[:7]):
        if char == 'B':
            low_row += math.ceil((high_row - low_row) / 2)
        if char == 'F':
            high_row -= math.ceil((high_row - low_row) / 2)

    for index, char in enumerate(line[-3:]):
        if char == 'R':
            low_c += math.ceil((high_c - low_c) / 2)
        if char == 'L':
            high_c -= math.ceil((high_c - low_c) / 2)
    seat_ids.append((low_row * 8 + low_c))

    seats[low_c].insert(low_row, low_row)
for index, columns in enumerate(seats):
    columns.sort()
    last_row = 0
    for row in columns:
        if last_row == 0:
            last_row = row
            continue
        if row == (last_row +1):
            last_row = row
            continue
        else:
            my_seat = (row -1)*8 + index +1
            last_row = row
seat_ids.sort(reverse=True)
print(my_seat)
print(seat_ids)
