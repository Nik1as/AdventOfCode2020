import re

insturctions = []

with open("8.txt") as f:
    insturctions = f.readlines()

pattern = re.compile("(acc|jmp|nop) ([+-][0-9]+)")

# 1
accomulator = 0
line = 0
executed_lines = set()

while line not in executed_lines:
    match = re.match(pattern, insturctions[line])
    operation = match.group(1)
    argument = int(match.group(2))

    executed_lines.add(line)

    if operation == "acc":
        accomulator += argument
        line += 1
    elif operation == "jmp":
        line += + argument
    elif operation == "nop":
        line += 1

print(accomulator)

# 2
for i in range(len(insturctions)):
    accomulator = 0
    line = 0
    executed_lines = set()
    instructions_copy = insturctions.copy()

    if instructions_copy[i].startswith("jmp"):
        instructions_copy[i] = instructions_copy[i].replace("jmp", "nop")
    elif instructions_copy[i].startswith("nop"):
        instructions_copy[i] = instructions_copy[i].replace("nop", "jmp")

    while line not in executed_lines:
        if line == len(instructions_copy) - 1:
            print(accomulator)
            quit()

        match = re.match(pattern, instructions_copy[line])
        operation = match.group(1)
        argument = int(match.group(2))

        executed_lines.add(line)

        if operation == "acc":
            accomulator += argument
            line += 1
        elif operation == "jmp":
            line += + argument
        elif operation == "nop":
            line += 1
