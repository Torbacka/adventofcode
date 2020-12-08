import re

parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in")]

bags = {}
colors = set()
for line in data:
    split = line.split(", ")
    bag_color = ""
    for i, color in enumerate(split):
        if 'contain' in color:
            color_split = color.split(" bags contain ")
            bag_color = color_split[0]
            inner_bag = color_split[1][2:]
            if "no other" in color_split[1]:
                continue
            if "bag" in inner_bag:
                inner_bag = inner_bag.split(" bag")[0]
            if "bag" in bag_color:
                bag_color = bag_color.split(" bag")[0]
            if bag_color in bags:

                bags[bag_color].update({
                    inner_bag: int(color_split[1][:2])
                })
            else:
                bags[bag_color] = {
                    inner_bag: int(color_split[1][:2])
                }
        else:
            inner_bag = color[2:]
            if "bag" in inner_bag:
                inner_bag = inner_bag.split(" bag")[0]
            bags[bag_color].update({
                inner_bag: int(color[:2])
            })


def count_bags(old_count, color, bags):
    if color not in bags:
        return 1
    count = old_count
    for color, amount in bags[color].items():
        count += count_bags(old_count, color, bags)*amount
    count +=1
    return count


count = count_bags(0, 'shiny gold', bags)
print(count-1)
