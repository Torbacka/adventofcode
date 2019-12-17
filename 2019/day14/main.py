import math
from typing import List


def main():
    total_ore = 1000000000000
    saved_reactants = {}
    reactions = parse_input()
    fuel = 0
    while total_ore > 0:
        ore = calculate_ore(reactions['FUEL'], saved_reactants, reactions)
        total_ore -= ore
        fuel += 1
    print(fuel)


def calculate_ore(reaction, saved_reactants, reactions):
    ore = 0
    for reactant, value in reaction['reactants'].items():
        if reactant == 'ORE':
            return reaction['reactants'][reactant]
        needed_amount, saved_reactants = calculate_amount_needed(reactant, value, reactions, saved_reactants)
        for i in range(needed_amount):
            ore += calculate_ore(reactions[reactant], saved_reactants, reactions)
    return ore


def calculate_amount_needed(reactant, value, reactions, saved_reactants):
    if reactant in saved_reactants:
        if value <= saved_reactants[reactant]:
            saved_reactants[reactant] -= value
            value = 0
        else:
            value -= saved_reactants[reactant]
            saved_reactants[reactant] = 0
    else:
        saved_reactants[reactant] = 0
    amount_needed = math.ceil(value / reactions[reactant]['amount'])
    if value % reactions[reactant]['amount'] != 0:
        saved_reactants[reactant] = (reactions[reactant]['amount'] * amount_needed) - value
    return amount_needed, saved_reactants


def parse_input():
    reactions = {}
    for line in open("input/input.in").readlines():
        reaction = line.split("=>")
        product = reaction[1].strip().split(" ")
        product_name = product[1].strip()
        reactions[product_name] = {'amount': int(product[0].strip())}
        reactants = reaction[0].split(",")
        for reactant in reactants:
            reactants_parts: List[str] = reactant.strip().split(" ")
            if 'reactants' in reactions[product_name]:
                reactions[product_name]['reactants'][reactants_parts[1].strip()] = int(reactants_parts[0].strip())
            else:
                reactions[product_name]['reactants'] = {reactants_parts[1].strip(): int(reactants_parts[0].strip())}
    return reactions


if __name__ == '__main__':
    main()
