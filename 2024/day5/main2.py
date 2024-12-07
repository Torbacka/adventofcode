data_rules, data_manuals = [M for M in open("input/input.in").read().split("\n\n")]
rules = [list(map(int, r.strip().split("|"))) for r in data_rules.split("\n")]
manuals = [list(map(int, m.strip().split(","))) for m in data_manuals.split("\n")]


def check_rule(rule, manual):
    if rule[0] > rule[1]:
        for i, value in enumerate(manual):
            if value != rule[0]:
                continue
            for i2 in range(0, i):
                if manual[i2] != rule[1]:
                    continue
                if value > manual[i2]:
                    return (i, i2), False
            break
    elif rule[0] < rule[1]:
        for i, value in enumerate(manual):
            if value != rule[0]:
                continue
            for i2 in range(0, i):
                if manual[i2] != rule[1]:
                    continue
                if value < manual[i2]:
                    return (i, i2), False
    return (-1,-1), True

print(check_rule([47, 53],[75, 53, 47, 61, 29]))
result = 0


def check_rules(manual):
    for rule in rules:
        coord, b = check_rule(rule, manual)
        if not b:
            manual[coord[0]], manual[coord[1]] = manual[coord[1]], manual[coord[0]]
            return manual, False
    return manual, True



for manual in manuals:
    safe = False
    found_unsafe = False
    while not safe:
        manual, safe = check_rules(manual)
        if not safe:
            found_unsafe = True
    if found_unsafe:
        result += int(manual[len(manual) // 2])




print(result)
