grid = [[l for l in line.strip()] for line in open("input/input.in").readlines()]
true_start = (0,0)
for y, line in enumerate(grid):
    for x, value in enumerate(line):
        if value == '^':
            true_start = (x, y)
            grid[true_start[1]][true_start[0]] = dir
start = true_start
result2 = 0
def check_boundary(x_1, y_1):
    return 0 <=  x_1 < len(grid[0]) and 0 <= y_1 < len(grid)

def draw_grid():
    for y, line in enumerate(grid):
        print()
        for x, value in enumerate(line):
            if value == (1,0) or value == (-1,0):
                print('-', end='')
            elif value == (0,1) or value == (0,-1):
                print('|', end='')
            else:
                print(value, end='')


def check_loop(old_dir,loop_dir, old_pos):
    loop_start = old_pos
    loop_dir_start = loop_dir
    path = {(loop_start, loop_dir_start)}
    while check_boundary(loop_start[0], loop_start[1]):
        new_start = (loop_start[0] + loop_dir[0], loop_start[1] + loop_dir[1])
        if not check_boundary(new_start[0], new_start[1]):
            return False
        if grid[new_start[1]][new_start[0]] == '#':
            loop_dir = (-loop_dir[1], loop_dir[0])
            new_start = (loop_start[0] + loop_dir[0], loop_start[1] + loop_dir[1])
        loop_start = new_start
        grid[loop_start[1]][loop_start[0]] = loop_dir

        if loop_start == old_pos and loop_dir == old_dir:
            return True
        elif loop_start == old_pos and loop_dir == loop_dir_start:
            return True
        elif (loop_start, loop_dir) in path:
            return True
        else:
            path.add((loop_start, loop_dir))

def walk(start, dir):
    global result2
    while check_boundary(start[0], start[1]):
        new_start = (start[0] + dir[0], start[1] + dir[1])
        if not check_boundary(new_start[0], new_start[1]):
            return False
        if grid[new_start[1]][new_start[0]] == '#':
            dir = (-dir[1], dir[0])
            grid[start[1]][start[0]] = dir
            new_start = (start[0] + dir[0], start[1] + dir[1])
        start = new_start
        grid[start[1]][start[0]] = dir
        loop_dir = (-dir[1], dir[0])
        if true_start != start and check_loop(dir, loop_dir, start):
            result2 += 1


dir = (0, -1)
walk(start, dir)

draw_grid()
print()
print(result2)
