import re
from functools import reduce

parser = re.compile("\d+")

data = open("input/input.in").read().split("\n\n")
rule_names = [rule.split(":")[0] for rule in data[0].split("\n")]
rules = [[int(x) for x in parser.findall(rule)] for rule in data[0].split("\n")]
my_ticket = data[1].split("\n")[1].split(",")
nearby_tickets = [ticket.split(",") for ticket in data[2].split("\n")[1:]]
valid_tickets = {}
error = []
for ticket in nearby_tickets:
    ticket_valid = True
    for number in ticket:
        number = int(number)
        valid = False
        for rule in rules:
            if rule[0] <= number <= rule[1]:
                valid = True
            elif rule[2] <= number <= rule[3]:
                valid = True
            if valid:
                break
        if not valid:
            ticket_valid = False
            error.append(number)
    if ticket_valid:
        for i, number in enumerate(ticket):
            if i not in valid_tickets:
                valid_tickets[i] = [number]
            else:
                valid_tickets[i].append(number)
mapping = {}
for position, ticket in valid_tickets.items():
    for number in ticket:
        number = int(number)
        valid_rule = set()
        for i, rule in enumerate(rules):
            valid = False
            if rule[0] <= number <= rule[1]:
                valid = True
            elif rule[2] <= number <= rule[3]:
                valid = True
            if valid:
                valid_rule.add(i)
        if position not in mapping:
            mapping[position] = valid_rule
        else:
            mapping[position] = mapping[position].intersection(valid_rule)

found = {}
while len(mapping) > 0:
    filtered_mappings = dict((key, value) for key, value in mapping.items() if len(value) == 1)
    found.update(filtered_mappings)
    for filtered_key, filtered_value in filtered_mappings.items():
        del mapping[filtered_key]
        for key, value in mapping.items():
            mapping[key] = mapping[key] - filtered_value

print(sum(error))
mult = []
for key, value in found.items():
    pop = value.pop()
    if pop <= 5:
        mult.append(int(my_ticket[key]))
print(reduce((lambda x, y: x * y), mult))
