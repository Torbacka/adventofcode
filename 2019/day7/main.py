import re
import itertools


def main():
    parser = re.compile("-?\d+")
    data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]
    phase_settings = list(itertools.permutations([5, 6, 7, 8, 9]))
    max_output = 0
    for settings in phase_settings:
        program_states = prepare_program_states(data, settings)
        while True:
            for i in range(len(settings)):
                program_states[i] = compute(program_states[i])
                if i + 1 < len(settings):
                    program_states[i + 1]['input'].append(program_states[i]['output'][-1])
                else:
                    print(f"Output: {program_states[i]['output'][-1]}")
                    program_states[0]['input'].append(program_states[i]['output'][-1])
            if all(value['done'] for value in program_states):
                break
        if program_states[-1]['output'][-1] > max_output:
            max_output = program_states[-1]['output'][-1]
    print(max_output)


def prepare_program_states(data, settings):
    program_states = []
    for setting in settings:
        program_states.append({
            'program': data[:],
            'input': [setting],
            'output': [],
            'pc': 0,
            'input_pointer': 0,
            'done': False
        })
    program_states[0]['input'].append(0)
    return program_states


def compute(program_state):
    input = program_state['input']
    data = program_state['program']
    output = program_state['output']
    pc = program_state['pc']  # Program counter
    input_pointer = program_state['input_pointer']
    while pc < len(data):
        program_string = str(data[pc])
        op_code = program_string[-2:].rjust(2, "0")
        parameter_modes = program_string[:-2]
        if op_code == "01":
            parameters = get_parameters(pc, data, 3, parameter_modes)
            data[parameters[2]] = data[parameters[0]] + data[parameters[1]]
            pc += 4
        elif op_code == "02":
            parameters = get_parameters(pc, data, 3, parameter_modes)
            data[parameters[2]] = data[parameters[0]] * data[parameters[1]]
            pc += 4
        elif op_code == "03":
            parameters = get_parameters(pc, data, 1, parameter_modes)
            if input_pointer >= len(input):
                program_state['pc'] = pc
                program_state['input_pointer'] = input_pointer
                return program_state
            data[parameters[0]] = input[input_pointer]
            input_pointer += 1
            pc += 2
        elif op_code == "04":
            parameters = get_parameters(pc, data, 1, parameter_modes)
            output.append(data[parameters[0]])
            pc += 2
        elif op_code == "05":  # Jump-if-true
            parameters = get_parameters(pc, data, 2, parameter_modes)
            if data[parameters[0]] != 0:
                pc = data[parameters[1]]
            else:
                pc += 3
        elif op_code == "06":  # Jump-if-false
            parameters = get_parameters(pc, data, 2, parameter_modes)
            if data[parameters[0]] == 0:
                pc = data[parameters[1]]
            else:
                pc += 3
        elif op_code == "07":  # Less than
            parameters = get_parameters(pc, data, 3, parameter_modes)
            if data[parameters[0]] < data[parameters[1]]:
                data[parameters[2]] = 1
            else:
                data[parameters[2]] = 0
            pc += 4
        elif op_code == "08":  # equals
            parameters = get_parameters(pc, data, 3, parameter_modes)
            if data[parameters[0]] == data[parameters[1]]:
                data[parameters[2]] = 1
            else:
                data[parameters[2]] = 0
            pc += 4
        elif op_code == "99":
            program_state['done'] = True
            break
        else:
            print("Halt and catch fire!!!")

    return program_state


def get_parameters(pc, data, number_of_parameters, parameter_modes):
    parameters = []
    # [::-1] is reversing string
    parameter_modes = parameter_modes.rjust(number_of_parameters, "0")[::-1]

    for i, mode in enumerate(parameter_modes, start=1):
        if mode == '0':
            parameters.append(data[pc + i])
        elif mode == '1':
            parameters.append(pc + i)
        else:
            print("Halt and catch fire!")
            break
    return parameters


if __name__ == '__main__':
    main()
