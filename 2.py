import re

lines = []

with open("2.txt") as f:
    lines = f.readlines()

pattern = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

# 1
valid_1 = 0
valid_2 = 0
for line in lines:
    match = re.match(pattern, line)
    min_amount = int(match.group(1))
    max_amount = int(match.group(2))
    char = match.group(3)
    password = match.group(4)

    if min_amount <= password.count(char) <= max_amount:
        valid_1 += 1

    if (password[min_amount - 1] == char) ^ (password[max_amount - 1] == char):
        valid_2 += 1

print(valid_1)
print(valid_2)
