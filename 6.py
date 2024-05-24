groups = []

with open("6.txt") as f:
    groups = f.read().split("\n\n")

# 1
counts = []
for group in groups:
    counts.append(len(set(group.replace("\n", ""))))

print(sum(counts))

# 2
counts = []
for group in groups:
    common_answers = set(group.split("\n")[0])
    for answers in group.split("\n"):
        common_answers.intersection_update(set(answers))
    counts.append(len(common_answers))

print(sum(counts))
