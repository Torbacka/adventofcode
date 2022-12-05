from functools import reduce

file = open("input.in").read()
lengths = [int(bytes(c, 'ascii')[0]) for c in file]
lengths.extend([17, 31, 73, 47, 23])
numbers = []
current = 0
skip_size = 0
for i in range(256):
    numbers.append(i)

for n in range(64):
    for length in lengths:
        wrap_pos = (length + current) % len(numbers)
        pos = []
        if length == 0:
            pass
        elif wrap_pos <= current:
            for i in range(current, len(numbers)):
                pos.append(i)
            for i in range(wrap_pos):
                pos.append(i)
        else:
            for i in range(current, wrap_pos):
                pos.append(i)
        temp = numbers.copy()
        for i, value in enumerate(pos):
            temp[pos[-i - 1]] = numbers[value]
        numbers = temp
        print(numbers)
        current = (current + length + skip_size) % len(numbers)
        skip_size += 1
output = ''
for i in range(0, len(numbers), 16):
    reduced_numbers = numbers[i:i + 16]
    hash_number = reduce(lambda i, j: int(i) ^ int(j), reduced_numbers)
    hash_string = f'{hash_number:x}'
    if len(hash_string) < 2:
        hash_string = f'0{hash_string}'
    output += hash_string
print(output)
