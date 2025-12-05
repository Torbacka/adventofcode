import re

parser = re.compile(r"-?\d+")
grid = [[l for l in line.strip()] for line in open("input/input.in").readlines()]
neighbours = [
    (1, 0),    # right
    (1, 1),    # down-right
    (0, 1),    # down
    (-1, 1),   # down-left
    (-1, 0),   # left
    (-1, -1),  # up-left
    (0, -1),   # up
    (1, -1)    # up-right
]

def printGrid():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='')
        print()
def remove_toilet_paper(grid):
    cells_to_remove = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            cell = grid[y][x]
            if cell != '@':
                print('.', end='')
                continue
            count = 0
            for dx, dy in neighbours:
                nx = x + dx
                ny = y + dy
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                    if grid[ny][nx] == '@':
                        count += 1
            if count < 4:
                cells_to_remove.append((x, y))
                print('X', end='')
            else:
                print('@', end='')
        print()
    return cells_to_remove

sum = 0
while True:
    cells_to_remove = remove_toilet_paper(grid)
    print()
    sum += len(cells_to_remove)
    if len(cells_to_remove) == 0:
        break
    for x, y in cells_to_remove:
        grid[y][x] = '.'
print(sum)