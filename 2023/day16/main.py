data = [line.strip() for line in open("input/input.in").readlines()]


def boundary_check(coordinate):
    global data
    len_y = len(data)
    len_x = len(data[0])
    return 0 <= coordinate[0] < len_x and 0 <= coordinate[1] < len_y


def print_grid(grid, energized):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if (x, y) in energized:
                print("#", end="")
            else:
                print(".", end="")
        print()


def energize_grid(direction, start, grid):
    starting_state = (direction, start)
    moves = [starting_state]
    memorized_moves = set()
    memorized_moves.add(starting_state)
    while len(moves) > 0:
        new_moves = []
        for directions, coordinate in moves:
            x, y = coordinate
            dx, dy = directions
            point = grid[y][x]
            if point == '/':
                dx = directions[1] * -1 if directions[0] == 0 else 0
                dy = directions[0] * -1 if directions[1] == 0 else 0
                coordinate = (x + dx, y + dy)
                memorized_move = ((dx, dy), coordinate)
                if boundary_check(coordinate) and memorized_move not in memorized_moves:
                    memorized_moves.add(memorized_move)
                    new_moves.append(memorized_move)
                continue
            elif point == '\\':
                dx = directions[1] if directions[0] == 0 else 0
                dy = directions[0] if directions[1] == 0 else 0
                coordinate = (x + dx, y + dy)
                memorized_move = ((dx, dy), coordinate)
                if boundary_check(coordinate) and memorized_move not in memorized_moves:
                    memorized_moves.add(memorized_move)
                    new_moves.append(memorized_move)
                continue
            elif point == '-':
                if dy != 0:
                    coordinate = (x + 1, y)
                    memorized_move = ((1, 0), coordinate)
                    if boundary_check(coordinate) and memorized_move not in memorized_moves:
                        memorized_moves.add(memorized_move)
                        new_moves.append(memorized_move)
                    coordinate = (x - 1, y)
                    memorized_move = ((-1, 0), coordinate)
                    if boundary_check(coordinate) and memorized_move not in memorized_moves:
                        memorized_moves.add(memorized_move)
                        new_moves.append(memorized_move)
                    continue
            elif point == '|':
                if dx != 0:
                    coordinate = (x, y + 1)
                    memorized_move = ((0, 1), coordinate)
                    if boundary_check(coordinate) and memorized_move not in memorized_moves:
                        memorized_moves.add(memorized_move)
                        new_moves.append(((0, 1), coordinate))
                    coordinate = (x, y - 1)
                    memorized_move = ((0, -1), coordinate)
                    if boundary_check(coordinate) and memorized_move not in memorized_moves:
                        memorized_moves.add(memorized_move)
                        new_moves.append(memorized_move)
                    continue

            coordinate = (x + dx, y + dy)
            memorized_move = ((dx, dy), coordinate)
            if boundary_check(coordinate) and memorized_move not in memorized_moves:
                memorized_moves.add(memorized_move)
                new_moves.append(memorized_move)
        moves = new_moves
    return memorized_moves


sums = 0
for n in range(len(data)):
    energized = len(set(point for _, point in energize_grid((1, 0), (0, n), data)))
    energized2 = len(set(point for _, point in energize_grid((-1, 0), (len(data[0]) - 1, n), data)))
    if energized > sums:
        sums = energized
    if energized2 > sums:
        sums = energized2
for m in range(len(data[0])):
    energized = set(point for _, point in energize_grid((0, 1), (m, 0), data))
    energized2 = len(set(point for _, point in energize_grid((0, -1), (m, len(data) - 1), data)))
    if len(energized) > sums:
        sums = len(energized)
    if energized2 > sums:
        sums = energized2

print(sums)
