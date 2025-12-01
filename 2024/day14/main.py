import re
from calendar import firstweekday

parser = re.compile(r"-?\d+")
width = 101
height = 103
bots = []
for bot in open('input/input.in').readlines():
    x, y, vx, vy = map(int, parser.findall(bot))
    bots.append(((x, y), (vx, vy)))

def display(bots):
    grid = []
    for h in range(height):
        grid.append([])
        for w in range(width):
            grid[h].append('.')
    for pos, vel in bots:
        grid[pos[1]][pos[0]] = 1 if grid[pos[1]][pos[0]] == '.' else (grid[pos[1]][pos[0]] + 1)
    for y, row in enumerate(grid):
        print()
        for x, v in enumerate(row):
            print(v, end='')

    print()
def wrapX(coord):
    if coord < 0:
        return width + coord
    elif coord >= width:
        return abs(width - coord)
    return coord


def wrapY(coord):
    if coord < 0:
        return height + coord
    elif coord >= height:
        return abs(height - coord)
    return coord


for i in range(10000):
    new_bots = []
    for position, velocity in bots:
        new_bots.append(((wrapX(position[0] + velocity[0]), wrapY(position[1] + velocity[1])), velocity))
    bots = new_bots
    display(bots)

first = []
second = []
third = []
fourth = []




display(bots)
for position, _ in bots:
    if 0 <= position[0] < (width // 2) and 0 <= position[1] < (height // 2):
        first.append(position)
    elif (width // 2) < position[0] < width and 0 <= position[1] < (height // 2):
        second.append(position)
    elif 0 <= position[0] < (width // 2) and (height // 2) < position[1] < height:
        third.append(position)
    elif (width // 2) < position[0] < width and (height // 2) < position[1] < height:
        fourth.append(position)
print()
print()
print(len(first)*len(second)*len(third)*len(fourth))
