import re

parser = re.compile(r"bag[s]?(?:[\s,.])?(?:contain)?")
data = [parser.split(line.strip()) for line in open("input/input.in")]

bags = {}
colors = set()
for line in data:
    split = line.split(", ")
    outer_bag = ""
    for i, color in enumerate(split):
        if 'contain' in color:
            color_split = color.split(" bags contain ")
            bag_color = color_split[1][2:]
            outer_bag = color_split[0]
            if "no other" in color_split[1]:
                continue
            if "bag" in bag_color:
                bag_color = bag_color.split(" bag")[0]
            if bag_color in bags:

                bags[bag_color].append(color_split[0])
            else:
                bags[bag_color] = [color_split[0]]
        else:
            bag_color = color[2:]
            if "bag" in bag_color:
                bag_color = bag_color.split(" bag")[0]
            if bag_color in bags:
                bags[bag_color].append(outer_bag)
            else:
                bags[bag_color] = [outer_bag]


def count_bags(count, colour, bags):
    if colour not in bags:
        return count
    count.update(bags[colour])
    for color in bags[colour]:
        count.update(count_bags(count, color, bags))
    return count


count = count_bags(set(), 'shiny gold', bags)
print(len(count))