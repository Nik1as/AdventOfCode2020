numbers = []

with open("1.txt") as f:
    numbers = list(map(int, f.readlines()))

# 1
for x in numbers:
    for y in numbers:
        if x + y == 2020:
            print(x * y)

# 2
for x in numbers:
    for y in numbers:
        for z in numbers:
            if x + y + z == 2020:
                print(x * y * z)
