import uuid
from collections import defaultdict

data = [line.strip() for line in open("input.in").readlines()]


def construct_disk():
    disk = defaultdict(dict)
    folder_path = "/"
    for line in data:
        command = line.split(" ")
        if command[0] == '$' and command[1] == 'cd':
            if command[2] == '..':
                folder_path = f"{folder_path.rsplit('/', 2)[0]}/"
            elif command[2] == '/':
                folder_path = '/'
            else:
                folder_path += f"{command[2]}/"
        elif command[0].isnumeric():
            disk['/'][uuid.uuid4()] = int(command[0])
            for splits in range(folder_path.count("/") - 1):
                directory = folder_path.rsplit('/', 1 + splits)[0]
                disk[directory][uuid.uuid4()] = int(command[0])
    return disk


def part_2():
    root_size = 0
    for sizes in disk['/'].values():
        root_size += sizes
    size_to_delete = 30000000 - (70000000 - root_size)
    dir_sizes = []
    for path, files in disk.items():
        dir_size = 0
        for _, size in files.items():
            dir_size += size
        if dir_size >= size_to_delete:
            dir_sizes.append(dir_size)
    print(f"part 2: {sorted(dir_sizes)[0]}")


def part_1():
    total_sum = sum([sum(folder.values()) for _, folder in disk.items() if sum(folder.values()) <= 100000])
    print(f"part 1: {total_sum}")


disk = construct_disk()
part_1()
part_2()
