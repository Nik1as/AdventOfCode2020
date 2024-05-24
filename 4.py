import re

fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
passports = []

with open("4.txt") as f:
    passports = f.read().split("\n\n")

# 1
valid = 0
for passport in passports:
    for field in fields:
        if field not in passport:
            break
    else:
        valid += 1

print(valid)


def height_check(s):
    if s.endswith("cm"):
        return 150 <= int(s[:-2]) <= 193
    elif s.endswith("in"):
        return 59 <= int(s[:-2]) <= 76
    return False


# 2
valid = 0
values = {
    "byr": lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
    "iyr": lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
    "eyr": lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
    "hgt": height_check,
    "hcl": lambda s: re.match("#[0-9a-f]{6}", s),
    "ecl": lambda s: s in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda s: len(s) == 9 and re.match("([0-9]){9}", s),
    "cid": lambda _: True
}
for passport in passports:
    for field in fields:
        if field not in passport:
            break
    else:
        for field in passport.replace("\n", " ").split(" "):
            tag = field.split(":")[0]
            value = field.split(":")[1]
            if not values[tag](value):
                break
        else:
            valid += 1

print(valid)
