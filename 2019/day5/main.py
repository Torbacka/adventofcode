import re


def main():
    parser = re.compile("-?\d+")
    data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]
    compute(data)


def compute(data):
    pc = 0  # Program counter
    input = 5
    output = []
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
            data[parameters[0]] = input
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
            break
        else:
            print("Halt and catch fire!!!")
    if all(n == 0 for n in output[:-1]):
        print(output[-1:])


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
