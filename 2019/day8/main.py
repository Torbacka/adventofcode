import re

data = map(int, open("input/input.in").readlines()[0][:])


def main():
    layers = []
    layer = []
    width = 25
    height = 6
    for i, number in enumerate(data):
        if layer and i % (width * height) == 0:
            layers.append(layer)
            layer = []
        layer.append(number)
    layers.append(layer)
    sorted_layers = sorted(layers, key=lambda sublist: accuracies(0, sublist))
    print(f"Solution part1: {accuracies(1, sorted_layers[0]) * accuracies(2, sorted_layers[0])}")
    for h in range(height):
        row = ""
        for w in range(width):
            pixel = layers[0][width * h + w]
            if pixel == 2:
                for i in range(1, len(layers)):
                    pixel = layers[i][width * h + w]
                    if pixel != 2:
                        break
            row += str(pixel) + " "
        print(row)


def accuracies(needle, sublist):
    return sum(number == needle for number in sublist)


if __name__ == '__main__':
    main()
