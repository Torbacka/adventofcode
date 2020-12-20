import math
import re
from copy import deepcopy

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

for corner_id, corner_tiles in rotate_data.items():
    for corner_tile in corner_tiles:
        image_found = False
        rotate_data_copy = deepcopy(rotate_data)
        del rotate_data_copy[corner_id]

        for i in range(1, square_len * square_len + 1):
            possible_tiles_dict = rotate_data_copy
            rotate_data_copy = dict()
            for possible_corner_id, possible_tiles in possible_tiles_dict.items():
                for possible_tile in possible_tiles:
                    left_check = False
                    if i % square_len > 0 or int(i / square_len) == 0:
                        if get_side(corner_tile, 0) == get_side(possible_tile, -1):
                            if possible_corner_id not in rotate_data_copy:
                                rotate_data_copy[possible_corner_id] = set()
                            left_check = True
                    right_check = None
                    if int(i / square_len) > 0 and ((i % square_len) == 0 or left_check):
                        if corner_tile[0] != possible_tile[-1]:
                            right_check = True
                    if (left_check and right_check is None) or (left_check and right_check):
                        rotate_data_copy[possible_corner_id].add(possible_tile)