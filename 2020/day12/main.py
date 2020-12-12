from math import cos, sin, radians

east = 0
north = 0
heading = 1
headings = ['N', 'E', 'S', 'W']
waypoint = [10, 1]


def rotate(d):
    global heading
    radian = radians(d)
    new_x = round(waypoint[0] * cos(radian) + waypoint[1] * sin(radian))
    new_y = round(-waypoint[0] * sin(radian) + waypoint[1] * cos(radian))
    waypoint[0] = new_x
    waypoint[1] = new_y


def update_distance(value, direction):
    global north, east
    if direction == 'N':
        waypoint[1] += value
    elif direction == 'S':
        waypoint[1] -= value
    elif direction == 'E':
        waypoint[0] += value
    elif direction == 'W':
        waypoint[0] -= value


for line in open("input/input.in"):
    action = line[:1]
    value = int(line[1:])
    if action == 'L':
        rotate(360 - value)
    elif action == 'R':
        rotate(value)
    elif action == 'F':
        north += value * waypoint[1]
        east += value * waypoint[0]
    else:
        update_distance(value, action)

print(abs(east) + abs(north))
