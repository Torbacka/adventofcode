import re

parser = re.compile(r"-?\d+")
data = open("input/input.in").read().split("\n\n")
rules = [list(map(int, line.strip().split("-"))) for line in data[0].split("\n")]
sorted_rules = sorted(rules, key=lambda r: r[0])
for index, rule in enumerate(sorted_rules):
    rules_copy = sorted_rules.copy()
    for i, rule2 in enumerate(rules_copy[index+1:]):
        if rule[1] >= rule2[0]:
            if rule[1] > rule2[1]:
                sorted_rules.remove(rule2)
            else:
                rule2[0] = rule[1] + 1


sum = 0
for low, high in sorted_rules:
    sum += high - low + 1
print(sum)
