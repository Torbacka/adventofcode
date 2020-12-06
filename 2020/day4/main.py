import re

passport = None
requireds = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]
count = 0
for line in open("input/input.in").readlines():

    if passport is None:
        passport = {data.split(":")[0]: data.split(":")[1] for data in line.split()}
    elif len(line) == 1:
        all_required = True
        valid = True
        for required in requireds:
            if required not in passport.keys():
                all_required = False
                break
            if required == 'hgt':
                unit = passport['hgt'][-2:]
                if unit == 'cm':
                    hgt = int(passport['hgt'][:-2])
                    if hgt < 150 or hgt > 193:
                        valid = False
                elif unit == 'in':
                    hgt = int(passport['hgt'][:-2])
                    if hgt < 59 or hgt > 76:
                        valid = False
                else:
                    valid = False
            elif required == 'byr':
                year = int(passport['byr'])
                if year < 1920 or year > 2002:
                    valid = False
            elif required == 'iyr':
                issue_year = int(passport['iyr'])
                if issue_year < 2010 or issue_year > 2020:
                    valid = False
            elif required == 'eyr':
                exp_year = int(passport['eyr'])
                if exp_year < 2020 or exp_year > 2030:
                    valid = False
            elif required == 'hcl':
                hair_color = passport['hcl']
                if hair_color[0] == '#' and len(hair_color[1:]) == 6:
                    match = re.match("#[0-9a-f]*", hair_color)
                    if match.endpos != 7:
                        valid = False
                else:
                    valid = False
            elif required == 'ecl':
                valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                eye_color = passport['ecl']
                if len(eye_color) != 3 or eye_color not in valid_colors:
                    valid = False
            elif required == 'pid':
                id = passport['pid']
                re_match = re.match('[0-9]*', id)
                if re_match.endpos != 9:
                    valid = False
        if all_required and valid:
            count += 1
        passport = None
    else:
        passport.update({data.split(":")[0]: data.split(":")[1] for data in line.split()})
print(count)
