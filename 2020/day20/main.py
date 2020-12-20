import math
import operator
import re
from collections import Counter
from copy import deepcopy
from functools import reduce

import numpy


def rotate(matrix):
    return zip(*matrix[::-1])


def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print(column, end="")
        print()


def get_side(matrix, i):
    return [row[i] for row in matrix]


def check_sides(matrix1, matrix2, corners_found):
    if Counter(matrix1[0]) == Counter(matrix2[-1]):
        corners_found[0] = 1
    if Counter(matrix1[-1]) == Counter(matrix2[0]):
        corners_found[1] = 1
    if Counter(get_side(matrix1, -1)) == Counter(get_side(matrix2, 0)):
        corners_found[3] = 1
    if Counter(get_side(matrix1, 0)) == Counter(get_side(matrix2, -1)):
        corners_found[2] = 1

    return corners_found


parser = re.compile("-?\d+")
tile_data = [[parser.findall(tile_data)[0], [list(pixel) for pixel in tile_data.split("\n")[1:]]] for tile_data in
             open("input/input.in").read().split("\n\n")]
square_len = math.floor(math.sqrt(len(tile_data)))
rotate_data = {}
for i, tile in enumerate(tile_data):
    tile_matrix = tile[1].copy()
    all_positions = set()
    for f in [-1, 0, 1, 0]:
        if f != -1:
            tile_matrix = numpy.flip(tile_matrix, f)
        rotate = tile_matrix.copy()
        for r in range(4):
            rotate = numpy.rot90(rotate)
            all_positions.add(tuple(map(tuple, rotate)))
    rotate_data[tile[0]] = all_positions
corner = set()

for tile_id, rotate_tile in rotate_data.items():
    image_found = False
    for top_corner in rotate_tile:
        grid = [{tile_id: [top_corner]}]
        column = 0
        rotate_data_copy = deepcopy(rotate_data)
        for i in [1, 2, 3, 4, 5, 6, 7, 8]:
            if len(grid) != i:
                break
            for key in grid[-1].keys():
                if key in rotate_data_copy:
                    del rotate_data_copy[key]
            for compare_id, compare_rotate_tile in rotate_data_copy.items():
                for tile in compare_rotate_tile:
                    left_check = False
                    if i % square_len > 0 or int(i / square_len) == 0:
                        for grid_id, compare_tiles in grid[i - 1].items():
                            for compare_tile in compare_tiles:
                                if get_side(tile, 0) == get_side(compare_tile, -1):
                                    if len(grid) == i:
                                        grid.append(dict())
                                    if compare_id not in grid[i]:
                                        grid[i][compare_id] = [tile]
                                        left_check = True
                    if int(i / square_len) > 0 and ((i % square_len) == 0 or left_check):
                        for grid_id, compare_tiles in grid[i - square_len].items():
                            for compare_tile in compare_tiles:
                                if tile[0] == compare_tile[-1]:
                                    if len(grid) == i:
                                        grid.append(dict())
                                    if compare_id not in grid[i]:
                                        grid[i][compare_id] = [tile]

            if len(grid) == 12:

                print("*****************************************")
                for y in range(square_len):
                    for x in range(square_len):
                        square = next(iter(grid[x + y * square_len]))
                        if (x == 0 and y == 0) or (x == square_len - 1 and y == 0) or (
                                x == 0 and y == square_len - 1) or (x == square_len - 1 and y == square_len - 1):
                            corner.add(int(square))
                        print(square, end="\t")
                    print()
                print("*****************************************")
                for y in range(3):
                    for inner in range(10):
                        for x in range(3):
                            square = next(iter(grid[x + y * square_len]))
                            print("".join(grid[x + y * square_len][square][0][inner]), end="")
                            print(" ", end="")
                        print()
                    print()
                print()
                image_found = True
        if image_found:
            break
    if image_found:
        break

print(corner)
print(reduce(operator.mul, corner))
