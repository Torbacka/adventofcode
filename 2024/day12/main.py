import math

from shapely import Polygon, LineString

grid = [[c for c in line.strip()] for line in open("input/input.in").readlines()]
neigbours_diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def findperimeter(fences):
    visited = set()
    count = 0
    for i in fences:
        if i in visited: continue
        count += 1
        x, y, diff_x2, diff_y2 = i
        queue = [(x, y)]
        visited.add((x, y, diff_x2, diff_y2))
        for x, y in queue:
            for diff_x, diff_y in neigbours_diff:
                new_x, new_y = x + diff_x, y + diff_y
                if (new_x, new_y, diff_x2, diff_y2) in fences and (new_x, new_y, diff_x2, diff_y2) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y, diff_x2, diff_y2))
    return count


# Example Usage

def check_boundary(pos):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)


def flood_fill(start, fence, plants):
    neighbours = []
    for diff in neigbours_diff:
        temp_pos = (start[0] + diff[0], start[1] + diff[1])
        if check_boundary(temp_pos) and grid[start[1]][start[0]] == grid[temp_pos[1]][
            temp_pos[0]] and temp_pos not in plants:
            neighbours.append(temp_pos)
    fence.extend([(start[0], start[1], diff[0], diff[1]) for diff in neigbours_diff if
                  not check_boundary((start[0] + diff[0], start[1] + diff[1])) or grid[start[1]][start[0]] !=
                  grid[start[1] + diff[1]][start[0] + diff[0]]])
    plants.update(neighbours)
    for neighbours in neighbours:
        fence, plants = flood_fill(neighbours, fence, plants)
    return fence, plants


sum = 0
plants = set()
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if (x, y) not in plants:
            plants.add((x, y))
            fence, p = flood_fill((x, y), [], {(x, y)})
            f = findperimeter(fence)
            plants.update(p)
            sum += f * len(p)
print(sum)
