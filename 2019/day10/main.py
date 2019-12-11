from sys import float_info

from sympy import Point, zoo


def main():
    data = parse_input()

    station = Point(27, 19)  # solution part 1
    slopes = {}
    for asteroid in data['asteroid']:
        if station == asteroid:
            continue
        slope = calculate_slope(station, asteroid)
        if slope in slopes:
            slopes[slope].append(asteroid)
        else:
            slopes[slope] = [asteroid]
    sort_asteroids(slopes, station)
    slopes[float_info.max] = slopes.pop(zoo)
    i = 1
    killed = []
    first_half = True
    while slopes.keys():
        for slope in sorted(slopes.keys(), reverse=True):
            print(slope)
            asteroids = []
            if first_half and slope >= 0:
                asteroids = list(filter(lambda asteroid: asteroid.x >= station.x and asteroid.y <= station.y, slopes[slope]))
            elif first_half and slope <= 0:
                asteroids = list(filter(lambda asteroid: asteroid.x >= station.x and asteroid.y >= station.y, slopes[slope]))
            elif not first_half and slope >= 0:
                asteroids = list(filter(lambda asteroid: asteroid.x <= station.x and asteroid.y >= station.y, slopes[slope]))
            elif not first_half and slope <= 0:
                asteroids = list(filter(lambda asteroid: asteroid.x <= station.x and asteroid.y <= station.y, slopes[slope]))
            if len(asteroids) == 0:
                continue
            asteroid = asteroids.pop(0)
            killed.append(asteroid)
            slopes[slope].remove(asteroid)
            if len(slopes[slope]) == 0:
                slopes.pop(slope)
            i += 1
        first_half = not first_half
    print((killed[199].x*100) + killed[199].y)


def find_slope(needle, slopes):
    for slope, asteroids in slopes.items():
        if needle in asteroids:
            return slope


def sort_slopes(slope1, slope2):
    if slope1 == zoo:
        slope1 = float_info.max
    if slope2 == zoo:
        slope2 = float_info.max
    return slope1 - slope2


def sort_asteroids(slopes, station):
    for value in slopes.values():
        value.sort(key=lambda x: sort_points(station, x))


def sort_points(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def calculate_slope(point1, point2):
    return - (point1.y - point2.y) / (point1.x - point2.x)


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
