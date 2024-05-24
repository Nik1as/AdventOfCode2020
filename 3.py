lines = []

with open("3.txt") as f:
    lines = [line.replace("\n", "") for line in f]

# 1
x = 0
trees = 0
right = 3
for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + right) % len(lines[0])

print(trees)

# 2
trees = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for right, down in slopes:
    t = 0
    x = 0
    y = 0
    while y < len(lines):
        if lines[y][x] == "#":
            t += 1
        y += down
        x = (x + right) % len(lines[0])
    trees.append(t)

product = 1
for t in trees:
    product *= t

print(product)
