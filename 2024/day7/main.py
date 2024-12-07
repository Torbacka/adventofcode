grid = [[l for l in line.strip()] for line in open("input/input.in").readlines()]
start = (0,0)
dir = (0, -1)
for y, line in enumerate(grid):
    for x, value in enumerate(line):
        if value == '^':
            start = (x, y)
            grid[start[1]][start[0]] = dir

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

result = 0
result2 = 0
while check_boundary(start[0], start[1]):
    new_start = (start[0]+dir[0], start[1] + dir[1])
    if not check_boundary(new_start[0], new_start[1]):
        break
    if grid[new_start[1]][new_start[0]] == '#':
        dir = (-dir[1], dir[0])
        grid[start[1]][start[0]] = dir
        new_start = (start[0] + dir[0], start[1] + dir[1])
    start = new_start
    grid[start[1]][start[0]] = dir

for y, line in enumerate(grid):
    for x, value in enumerate(line):
        if value == 'X' or value == '^':
            result += 1
draw_grid()
print()
print(result)
print(result2)
