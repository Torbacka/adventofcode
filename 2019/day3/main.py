from functools import cmp_to_key

from sympy import Point, Line, intersection

input = [line.split(",") for line in open("input/input.txt").readlines()]


def main():
    point_first = create_points(input[0])
    point_second = create_points(input[0])
    both = set(point_first.keys()) & set(point_second.keys())
    print(both)


def create_points(path):
    points = []
    point1 = (0, 0)
    for point in path:
        direction = point[:1]
        distance = int(point[1:])
        if direction == 'R':
            for i in range(distance):
                points.append((point1[0] + i, point1[1]))
            point1 = Point(point1[0] + distance, point1[1])
        elif direction == 'L':
            for i in range(distance):
                points.append((point1[0] - i, point1[1]))
            point1 = Point(point1[0] - distance, point1[1])
        elif direction == 'U':
            for i in range(distance):
                points.append((point1[0], point1[1] + i))
            point1 = Point(point1[0], point1[1] + distance)
        elif direction == 'D':
            for i in range(distance):
                points.append((point1[0], point1[1] - i))
            point1 = (point1[0], point1[1] - distance)
        else:
            print(f"Something when horrible wrong! {direction} {distance}")
    return points

if __name__ == '__main__':
    main()
