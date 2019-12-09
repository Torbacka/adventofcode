import re
import itertools


def main():
    parser = re.compile("-?\d+")
    data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]
    program_states = prepare_program_states(data, [[2]])
    state = compute(program_states[0])
    print(state['output'][-1])


def prepare_program_states(data, settings):
    program_states = []
    for setting in settings:
        program_state = prepare_program_state(data)
        program_state['input'] = setting
        program_states.append(program_state)
    return program_states


def prepare_program_state(data):
    program = {i: number for i, number in enumerate(data)}
    return {
        'program': program,
        'input': [],
        'output': [],
        'pc': 0,
        'input_pointer': 0,
        'relative_base': 0,
        'done': False
    }


def compute(program_state):
    data = program_state['program']
    output = program_state['output']
    while program_state['pc'] < len(data):
        program_string = str(data[program_state['pc']])
        op_code = program_string[-2:].rjust(2, "0")
        parameter_modes = program_string[:-2]
        if op_code == "01":
            parameters = get_parameters(program_state, data, 3, parameter_modes)
            products = get_products(data, parameters)
            data[parameters[2]] = products[0] + products[1]
            program_state['pc'] += 4
        elif op_code == "02":
            parameters = get_parameters(program_state, data, 3, parameter_modes)
            products = get_products(data, parameters)
            data[parameters[2]] = products[0] * products[1]
            program_state['pc'] += 4
        elif op_code == "03":
            parameters = get_parameters(program_state, data, 1, parameter_modes)
            if program_state['input_pointer'] >= len(program_state['input']):
                return program_state
            data[parameters[0]] = program_state['input'][program_state['input_pointer']]
            program_state['input_pointer'] += 1
            program_state['pc'] += 2
        elif op_code == "04":
            parameters = get_parameters(program_state, data, 1, parameter_modes)
            output.append(data[parameters[0]])
            program_state['pc'] += 2
        elif op_code == "05":  # Jump-if-true
            parameters = get_parameters(program_state, data, 2, parameter_modes)
            if data[parameters[0]] != 0:
                program_state['pc'] = data[parameters[1]]
            else:
                program_state['pc'] += 3
        elif op_code == "06":  # Jump-if-false
            parameters = get_parameters(program_state, data, 2, parameter_modes)
            if data[parameters[0]] == 0:
                program_state['pc'] = data[parameters[1]]
            else:
                program_state['pc'] += 3
        elif op_code == "07":  # Less than
            parameters = get_parameters(program_state, data, 3, parameter_modes)
            if data[parameters[0]] < data[parameters[1]]:
                data[parameters[2]] = 1
            else:
                data[parameters[2]] = 0
            program_state['pc'] += 4
        elif op_code == "08":  # equals
            parameters = get_parameters(program_state, data, 3, parameter_modes)
            if data[parameters[0]] == data[parameters[1]]:
                data[parameters[2]] = 1
            else:
                data[parameters[2]] = 0
            program_state['pc'] += 4
        elif op_code == "09":  # relative base offset
            parameters = get_parameters(program_state, data, 1, parameter_modes)
            program_state['relative_base'] += data[parameters[0]]
            program_state['pc'] += 2
        elif op_code == "99":
            program_state['done'] = True
            break
        else:
            print("Halt and catch fire!!!")

    return program_state


def get_products(data, parameters):
    value1, value2 = 0, 0
    if parameters[0] in data.keys():
        value1 = data[parameters[0]]
    if parameters[1] in data.keys():
        value2 = data[parameters[1]]
    return value1, value2


def get_parameters(program_state, data, number_of_parameters, parameter_modes):
    parameters = []
    pc = program_state['pc']
    # [::-1] is reversing string
    parameter_modes = parameter_modes.rjust(number_of_parameters, "0")[::-1]

    for i, mode in enumerate(parameter_modes, start=1):
        if mode == '0':  # position mode
            parameters.append(data[pc + i])
        elif mode == '1':  # immediate mode
            parameters.append(pc + i)
        elif mode == '2':  # relative mode
            parameters.append(data[pc + i] + program_state['relative_base'])
        else:
            print("Halt and catch fire!")
            break
    return parameters


if __name__ == '__main__':
    main()
