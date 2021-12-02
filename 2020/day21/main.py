from copy import deepcopy


def parse_line(line):
    return line.split(" (contains ")[1][:-1].strip(), line.split(" (contains ")[0]


data = [parse_line(line.strip()) for line in open("input/input.in")]

allergens = dict()

for allergen_list, ingredients in data:
    for allergen in allergen_list.split(", "):
        if allergen not in allergens:
            allergens[allergen] = set(ingredients.split())
        else:
            allergens[allergen] = allergens[allergen].intersection(ingredients.split())

while len([v for v in allergens.values() if len(v) > 1]):
    for allergen in [v for k, v in allergens.items() if len(v) == 1]:
        for k, v in allergens.items():
            if len(v) > 1:
                allergens[k] = v - allergen

set_of_allergens = {ingredients.pop() for ingredients in deepcopy(allergens).values()}
print(sum([len(set(ingredients.split()) - set_of_allergens) for _, ingredients in data]))
print(",".join([list(allergens[key])[0] for key in sorted(allergens.keys())]))
