import re

parser = re.compile("-?\d+")
rules = {line.split(":")[0]: line.split(":")[1].strip().replace("\"", "") for line in
         open("input/input.in").read().split("\n\n")[0].split("\n")}
inputs = open("input/input.in").read().split("\n\n")[1].split("\n")


def check_rule(rule_index, input):
    rule = rules[rule_index]
    if input[0] == '':
        input[0] = -1
        return input
    if input[0][0] == rule:
        return [input[0][1:]]
    elif rule != 'a' and rule != 'b':
        for sub_rules in rule.split("|"):
            temp = input.copy()
            loop11 = 0
            for sub_rule_index in sub_rules.strip().split(" "):
                temp = check_rule(sub_rule_index, temp)
                while ((rule_index == '8' and sub_rule_index == '42') or (
                        rule_index == '11' and (sub_rule_index == '42' or (sub_rule_index == '31' and loop11 > 0)))) and temp[0] != -1:
                    temp2 = check_rule(sub_rule_index, temp.copy())
                    if temp2[0] != -1:
                        if sub_rule_index =='42':
                            loop11+=1
                        else:
                            loop11 -=1
                        temp2.extend(temp)
                        temp = temp2
                    else:
                        break

                if temp[0] == -1:
                    break
            if temp[0] != -1:
                return temp
        return temp
    else:
        input[0] = -1
        return input


sum = 0
for input in inputs:
    temp = [input]
    for rule_index in rules['0'].split(" "):
        ret = []
        temp2 = temp.copy()
        temp = []
        while temp2:
            i = temp2.pop()
            ret = check_rule(rule_index, [i])
            if ret[0] != -1:
                temp.extend(ret)
    if '' in temp:
        print(input)
        sum += 1
print(sum)
