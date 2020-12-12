import copy

offset = [0, -1, 1]


def check_seat(x, y, level):
    occupied_sets = 0
    for y_offset in offset:
        if 0 <= y + y_offset < len(level):
            for x_offset in offset:
                if x_offset == 0 and y_offset == 0:
                    continue
                if 0 <= x + x_offset < len(level[y]):
                    y_distant = y_offset
                    x_distant = x_offset
                    while (level[y + y_distant][x + x_distant] == '.') and y_distant < 5 and x_distant < 5:
                        if not (0 <= x + x_distant + x_offset <= (len(level[y]) -1) and 0 <= y + y_distant + y_offset<= len(level) -1):
                            break
                        y_distant += y_offset
                        x_distant += x_offset
                    if 0 <= x + x_distant < len(level[y]) and 0 <= y + y_distant < len(level):
                        if level[y + y_distant][x + x_distant] == '#':
                            occupied_sets += 1
    return occupied_sets


level = [list(line.strip()) for line in open("input/input.in")]
changed = True
levels = 0
while changed:
    changed = False
    new_level = copy.deepcopy(level)
    for y, row in enumerate(level):
        for x, value in enumerate(row):
            if value == '.':
                continue
            occupied_sets = check_seat(x, y, level)
            if value == 'L' and occupied_sets == 0:
                changed = True
                new_level[y][x] = '#'
            elif value == '#' and occupied_sets >= 5:
                new_level[y][x] = 'L'
                changed = True
    level = new_level
occupied_seats = 0
for y, row in enumerate(level):
    for x, value in enumerate(row):
        if value == '#':
            occupied_seats += 1
print(occupied_seats)
