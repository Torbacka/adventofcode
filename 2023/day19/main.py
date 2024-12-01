import re
from collections import defaultdict

parser = re.compile("-?\d+")

graph = defaultdict(dict)
for line in open("input/input.in").read().strip().split("\n\n")[0].split("\n"):
    line = line[:-1]
    name, workflow = line.strip().split("{")
    rules = workflow.strip().split(",")
    dict_rules = []
    for rule in rules[:-1]:
        dict_rules.append({
            "variable": rule[0],
            "expression": rule.split(":")[0],
            "true": rule.split(":")[1]
        })
    graph[name] = {
        "false": rules[-1],
        "rules": dict_rules
    }
    print()

data = [[int(x.strip().split("=")[1]) for x in line.strip()[1:-1].strip().split(",")] for line in
        open("input/input.in").read().strip().split("\n\n")[1].split("\n")  ]


def evaluate(start, line):
    if start == "R" or start == "A":
        return start
    workflow = graph[start]
    x, m, a, s = line
    for rule in workflow["rules"]:
        if eval(rule["expression"]):
            return evaluate(rule["true"], line)
    return evaluate(workflow["false"], line)

sums = 0
for line in data:
    if evaluate('in', line) == "A":
        sums += sum(line)
print(sums)
