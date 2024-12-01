from collections import defaultdict
import sys

with open("input/input.in") as f: file = f.read()
lines, ans = file.split('\n'), 0


def north(grid):
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            cur = grid[row][col]
            if cur == 'O':
                for i in range(row - 1, -1, -1):
                    next = grid[i][col]
                    if next == '.':
                        grid[i + 1][col], grid[i][col] = '.', 'O'
                    else:
                        break
    return grid


def south(grid):
    for col in range(len(grid[0])):
        for row in range(len(grid) - 1, -1, -1):
            cur = grid[row][col]
            if cur == 'O':
                for i in range(row + 1, len(grid)):
                    next = grid[i][col]
                    if next == '.':
                        grid[i - 1][col], grid[i][col] = '.', 'O'
                    else:
                        break
    return grid


def west(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cur = grid[row][col]
            if cur == 'O':
                for i in range(col - 1, -1, -1):
                    next = grid[row][i]
                    if next == '.':
                        grid[row][i + 1], grid[row][i] = '.', 'O'
                    else:
                        break
    return grid


def east(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0]) - 1, -1, -1):
            cur = grid[row][col]
            if cur == 'O':
                for i in range(col + 1, len(grid[0])):
                    next = grid[row][i]
                    if next == '.':
                        grid[row][i - 1], grid[row][i] = '.', 'O'
                    else:
                        break
    return grid


grid, cache = [[c for c in line] for line in lines], {}

for i in range(1000000000):
    grid = east(south(west(north(grid))))
    key = ''
    for row in grid: key += ''.join(row)
    if key in cache:
        a, b = i - cache[key], cache[key]
        c = a * (1000000000 // a) + b
        if c > 1000000000: c -= a
        d = 1000000000 - c
        for i in range(d - 1):
            grid = east(south(west(north(grid))))
        break
    cache[key] = i

print(sum((len(grid) - i) * row.count('O') for i, row in enumerate(grid)))
