lines: list[str]
with open("inputs/day1.txt") as f:
    lines = f.readlines()


ids1: list[int] = []
ids2: list[int] = []
for line in lines:
    split = line.split("   ")
    ids1.append(int(split[0]))
    ids2.append(int(split[1]))

ids1.sort()
ids2.sort()
total = 0
for i, id in enumerate(ids1):
    total += abs(id - ids2[i])

print(total)
