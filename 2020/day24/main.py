import re

parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in")]

flipped = set()
for line in data:
    direction = ''
    coordinate = [0.0, 0.0]  # x,y
    for c in line:
        direction += c
        if len(direction) >= 3:
            print("FUUUU")
            break
        if direction == 'e':
            coordinate[0] += 1
            direction = ''
        elif direction == 'se':
            coordinate[0] += 0.5
            coordinate[1] -= 1
            direction = ''
        elif direction == 'sw':
            coordinate[0] -= 0.5
            coordinate[1] -= 1
            direction = ''
        elif direction == 'w':
            coordinate[0] -= 1
            direction = ''
        elif direction == 'nw':
            coordinate[0] -= 0.5
            coordinate[1] += 1
            direction = ''
        elif direction == 'ne':
            coordinate[0] += 0.5
            coordinate[1] += 1
            direction = ''
    flipped_coord = (coordinate[0], coordinate[1])
    if flipped_coord in flipped:
        flipped.remove(flipped_coord)
    else:
        flipped.add(flipped_coord)
black_tiles = flipped
for i in range(100):
    x_coordinates = [coordinate[0] for coordinate in flipped]
    y_coordinates = [coordinate[1] for coordinate in flipped]
    x_max = max(x_coordinates)
    x_min = min(x_coordinates)
    y_max = max(y_coordinates)
    y_min = min(y_coordinates)
    new_black_tiles = set()


    def get_neighbours(coord):
        return {(coord[0] + 1, coord[1]), (coord[0] + 0.5, coord[1] + 1), (coord[0] - 0.5, coord[1] + 1),
                (coord[0] - 1, coord[1]), (coord[0] - 0.5, coord[1] - 1), (coord[0] + 0.5, coord[1] - 1)}


    for y in range(round(y_min -100), round(y_max + 100)):
        x_modifier = 0
        if y % 2 != 0:
            x_modifier += 0.5
        for x in range(round(x_min -100), round(x_max + 100)):
            current_coord = (x + x_modifier, y)
            neighbours = get_neighbours(current_coord)
            black_neighbours = 0
            for neighbour in neighbours:
                if neighbour in black_tiles:
                    black_neighbours += 1
            if current_coord in black_tiles:
                if 0 < black_neighbours <= 2:
                    new_black_tiles.add(current_coord)
            else:
                if black_neighbours == 2:
                    new_black_tiles.add(current_coord)
    black_tiles = new_black_tiles
    print(f"{i+1}  {len(black_tiles)}")
print()