numbers = []

with open("9.txt") as f:
    numbers = list(map(int, f.readlines()))

for i in range(25, len(numbers) - 1):
    s = numbers[i - 24:i]
    for n in s:
        if s.count(numbers[i + 1] - n) >= 1:
            break
    else:
        print(numbers[i + 1])
        quit()
