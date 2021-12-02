from utils import *

numbers = [int(line) for line in open("input/input.in").readlines()]


if __name__ == '__main__':
    print(sum([int(b) > int(a) for a, b in zip(numbers, input[1:])]))
    print(sum([int(b) > int(a) for a, b in zip(numbers, input[3:])]))
