import re


program = [(line.split()[0], int(line.split()[1])) for line in open("input/input.in")]
nop_jmp = []

for i, instruction in enumerate(program):
    if instruction[0] == 'jmp' or instruction[0] == 'nop':
        nop_jmp.append(i)

for i in nop_jmp:
    program_counter = 0
    acc = 0
    executed = set()
    while True:
        if program_counter in executed:
            break
        elif program_counter == len(program):
            print(acc)
            break
        else:
            executed.add(program_counter)
        instruction = program[program_counter]
        if instruction[0] == 'acc':
            acc += instruction[1]
        elif (instruction[0] == 'jmp' and program_counter != i) or (instruction[0] == 'nop' and program_counter == i):
            program_counter += instruction[1]
            program_counter -= 1
        program_counter += 1
