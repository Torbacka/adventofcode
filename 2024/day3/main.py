import re
data = [line.strip() for line in open("input/input.in").readlines()]

def calculate_enabled_mul_sum(memory):
    enabled = True
    total = 0

    pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
    matches = re.findall(pattern, memory)

    for match in matches:
        instruction, a, b = match

        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul(") and enabled:
            total += int(a) * int(b)
    return total
result = 0
for line in data:
    result += calculate_enabled_mul_sum(line)
print(result)

