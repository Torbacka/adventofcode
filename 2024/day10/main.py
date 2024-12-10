grid = [[-1 if c == '.' else int(c) for c in line.strip()] for line in open("input/input.in").readlines()]
start_pos = [(x, y) for y, line in enumerate(grid) for x, value in enumerate(line) if value == 0]
neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def check_boundary(x_1, y_1):
    return 0 <= x_1 < len(grid[0]) and 0 <= y_1 < len(grid)


def walk_graph(start, true_start, score):
    hight = grid[start[1]][start[0]]
    if hight == 9:
        score.add((true_start, start))
        return score
    for neighbour_diff in neighbours:
        neighbour = (start[0] + neighbour_diff[0], start[1] + neighbour_diff[1])
        if check_boundary(neighbour[0], neighbour[1]):
            neighbour_high = grid[neighbour[1]][neighbour[0]]
            if neighbour_high == hight + 1:
                score = walk_graph(neighbour, true_start, score)
    return score

sum = 0
for start in start_pos:
    sum += len(walk_graph(start, start, set()))
print(sum)
