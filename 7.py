import re

rules = []

with open("7.txt") as f:
    rules = f.readlines()

graph = {}
for r in rules:
    color_primary = re.match(r"(.+?) bags", r).group(1)
    colors_inside = re.findall(r"(\d+) (.+?) bag", r)
    if len(colors_inside) > 0:
        graph[color_primary] = colors_inside
    else:
        graph[color_primary] = [("0", "")]


#  1
def contains_shiny(color):
    if color == "shiny gold":
        return True
    elif color == "":
        return False
    else:
        return any(contains_shiny(child) for amount, child in graph[color])


print(sum(contains_shiny(color) for color in graph.keys()) - 1)


# 2
def count(color):
    if color == "":
        return 1
    return 1 + sum(int(amount) * count(child) for amount, child in graph[color])


print(count("shiny gold") - 1)
