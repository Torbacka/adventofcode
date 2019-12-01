import re

parser = re.compile("-?\d+")
data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]

tree = dict()


def main():
    metadata = parse_tree(data.pop(0), data.pop(0), list(), data)
    print(sum(metadata))


def parse_tree(number_of_children, number_of_metadata, metadata, data):
    if number_of_children == 0:
        return sum(data[:number_of_metadata]), data[number_of_metadata:]
    for child in range(number_of_children):
        pair = parse_tree(data.pop(0), data.pop(0), metadata, data)
        metadata.extend(pair[0])
        data = pair[1]
    if len(data[number_of_metadata:]) == 0:
        metadata.extend(data[:number_of_metadata])
        return metadata
    return data[:number_of_metadata], data[number_of_metadata:]


if __name__ == '__main__':
    main()
