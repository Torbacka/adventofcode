import re
from collections import deque

parser = re.compile(r"-?\d+")
grid = [[l for l in line.strip()] for line in open("input/input.in").readlines()]
right = (1, 0)
left = (-1, 0)
down = (0, 1)


def simulate(start, direction):
    """
    Simulate the quantum tachyon manifold, but instead of tracking each
    individual particle, track how many timelines share the same state.

    This turns the exponential splitter growth into a dynamic program
    over (x, y, direction), which is at most O(width * height) states.
    """
    # Encode directions so they can be used in a small dict/tuple key.
    RIGHT, DOWN = 0, 1
    dir_vec = {
        RIGHT: right,
        DOWN: down,
    }

    # Map (x, y, dir_id) -> count of timelines in that exact state.
    states = {(*start, RIGHT if direction == right else DOWN): 1}
    finished = 0
    height = len(grid)
    width = len(grid[0]) if grid else 0

    while states:
        new_states = {}
        for (x, y, dir_id), count in states.items():
            dx, dy = dir_vec[dir_id]
            nx, ny = x + dx, y + dy

            # If we move past the bottom, all these timelines finish.
            if ny >= height:
                finished += count
                continue

            cell = grid[ny][nx]

            if cell == '.':
                key = (nx, ny, dir_id)
                new_states[key] = new_states.get(key, 0) + count
            elif cell == 'S':
                key = (nx, ny, DOWN)
                new_states[key] = new_states.get(key, 0) + count
            elif cell == '^':
                # Split into left and right paths, both going down.
                # Right split
                rx, ry = advance((nx, ny), right)
                rkey = (rx, ry, DOWN)
                new_states[rkey] = new_states.get(rkey, 0) + count

                # Left split
                lx, ly = advance((nx, ny), left)
                lkey = (lx, ly, DOWN)
                new_states[lkey] = new_states.get(lkey, 0) + count
            else:
                raise ValueError(f"Unexpected cell character: {cell}")

        states = new_states

    return finished


def advance(pos, direction):
    x, y = pos
    dx, dy = direction
    return x + dx, y + dy


print(simulate((0, 0), right))
