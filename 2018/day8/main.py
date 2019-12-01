import re

parser = re.compile("-?\d+")
data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]
node_name = 'A'


def main():
    tree = parse_tree(data.pop(0), data.pop(0), dict(), data)


    print(sum_tree(tree, 0))


def sum_tree(root, total_sum):
    tree = next(iter(root.values()))
    if len(tree['children']) == 0:
        return sum(tree['metadata'])
    else:
        for data in tree['metadata']:
            if len(tree['children']) < data:
                return 0
            else:
                total_sum += sum_tree(tree['children'][data - 1], total_sum)
    return total_sum


def parse_tree(number_of_children, number_of_metadata, tree, data):
    global node_name
    tree = dict()
    current_node = node_name
    if number_of_children == 0:
        tree[node_name] = {
            'metadata': data[:number_of_metadata],
            'children': []
        }
        return tree, data[number_of_metadata:]
    for child in range(number_of_children):
        if current_node not in tree.keys():
            tree[current_node] = {
                'metadata': [],
                'children': []
            }
        node_name = chr(ord(node_name) + 1)
        pair = parse_tree(data.pop(0), data.pop(0), tree, data)
        tree[current_node]['children'].append(pair[0])
        data = pair[1]
    tree[current_node]['metadata'] = data[:number_of_metadata]
    if len(data[number_of_metadata:]) == 0:
        return tree
    return tree, data[number_of_metadata:]


if __name__ == '__main__':
    main()
