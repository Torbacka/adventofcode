import sys

from sympy import Point, zoo
from sys import float_info


def main():
    data = parse_input()
    empty_score = {}
    for station in data['asteroid']:
        slopes = {}
        seen = set()
        for asteroid in data['asteroid']:
            if station == asteroid:
                continue
            slope = calculate_slope(station, asteroid)
            if slope in slopes:
                slopes[slope].append(asteroid)
            else:
                slopes[slope] = [asteroid]
        sort_slopes(slopes, station)
        seen.update([slopes[0] for slopes in slopes.values()])
        seen.update(one_to_the_side(slopes, station))
        for slope in slopes.values():
            if len(slope) > 0:
                seen.update(check_left_and_right(slope, station))
        empty_score[station] = len(seen)
    empty_score = {k: v for k, v in sorted(empty_score.items(), key=lambda item: item[1], reverse=True)}
    print(empty_score)


def check_left_and_right(slope, station):
    seen = set()
    if 0 == slope:
        zero_slopes = slope
        if len(zero_slopes) > 1:
            counted = zero_slopes[0]
            if station.x > counted.x:
                asteroid = next((asteroid for asteroid in zero_slopes if station.x < asteroid.x), None)
                if asteroid is not None:
                    seen.add(asteroid)
            elif station.x < counted.x:
                asteroid = next((asteroid for asteroid in zero_slopes if station.x > asteroid.x), None)
                if asteroid is not None:
                    seen.add(asteroid)
    else:
        if len(slope) > 1:
            counted = slope[0]
            if station.y > counted.y:
                asteroid = next((asteroid for asteroid in slope if station.y < asteroid.y), None)
                if asteroid is not None:
                    seen.add(asteroid)
            elif station.y < counted.y:
                asteroid = next((asteroid for asteroid in slope if station.y > asteroid.y), None)
                if asteroid is not None:
                    seen.add(asteroid)
    return seen


def one_to_the_side(slopes, station):
    seen = set()
    not_seen = [slope for slopes in slopes.values() for slope in slopes[1:]]
    for asteroid in not_seen:
        if (station.x == asteroid.x + 1 or station.x == asteroid.x - 1) and station.y == asteroid.y:
            seen.add(asteroid)
        elif (station.y == asteroid.y + 1 or station.y == asteroid.y - 1) and station.x == asteroid.x:
            seen.add(asteroid)
    return seen


def sort_slopes(slopes, station):
    for value in slopes.values():
        value.sort(key=lambda x: sort_points(station, x))


def sort_points(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def calculate_slope(point1, point2):
    return (point1.y - point2.y) / (point1.x - point2.x)


def parse_input():
    empty = []
    asteroid = []
    for y, line in enumerate(open("input/input.in").readlines()):
        for x, character in enumerate(line):
            if character == '.':
                empty.append(Point(x, y))
            elif character == '#':
                asteroid.append(Point(x, y))
            elif character == '\n':
                continue
            else:
                print("Halt and catch fire!!")
                exit(1)
    return {'asteroid': asteroid, 'empty': empty}


if __name__ == '__main__':
    main()
