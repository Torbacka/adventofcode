import math
import re

parser = re.compile(r"-?\d+")
dots = [tuple(map(int, parser.findall(line))) for line in open("input/input.in").readlines()]
print()


def merge_overlapping_sets(circuits):
    merged = True

    while merged:
        merged = False
        results = list()

        for n, circuit in enumerate(circuits):
            results.append(circuit)
            for circuit2 in circuits[n + 1:]:
                for dot in circuit:
                    if dot in circuit2:
                        results[-1] = results[-1].union(circuit2)
                        merged = True
                        circuits.remove(circuit2)
                        break
        circuits = results

    return circuits


def distance(dot, dot2):
    return math.sqrt(
        math.pow((dot[0] - dot2[0]), 2) + math.pow((dot[1] - dot2[1]), 2) + math.pow((dot[2] - dot2[2]), 2))


distances = []

for i, dot in enumerate(dots):
    for dot2 in dots[i:]:
        if dot == dot2:
            continue
        distances.append((dot, dot2, distance(dot, dot2)))

distances = sorted(distances, key=lambda x: x[-1])

circuits = set()
for dot, dot2, distance in distances:
    circuits.add(dot)
    circuits.add(dot2)

circuits = [{circuit} for circuit in circuits]

for i in range(10):
    #Pick sortest distance and process
    dot, dot2, distance = distances[i]
    found_circuit = False
    for circuit in circuits:
        if dot in circuit:
            circuit.add(dot2)
            # Check if dot2 is part of any other circuits and merge them
            for circuit2 in circuits:
                if  circuit != circuit2 and dot2 in circuit2:
                    circuit.union(circuit2)
                    circuits.remove(circuit2)

        elif dot2 in circuit:
            circuit.add(dot)
            found_circuit = True
            # Check if dot is part of any other circuits and merge them
            for circuit2 in circuits:
                if  circuit != circuit2 and dot in circuit2:
                    circuit.union(circuit2)
                    circuits.remove(circuit2)


circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
print(len(circuits[0]) * len(circuits[1]) * len(circuits[3]))
