from collections import defaultdict


lines: list[str]
with open("inputs/day1.txt") as f:
    lines = f.readlines()


ids1: list[int] = []
ids2: list[int] = []
for line in lines:
    split = line.split("   ")
    ids1.append(int(split[0]))
    ids2.append(int(split[1]))


def part1():
    ids1.sort()
    ids2.sort()
    total = 0
    for i, id in enumerate(ids1):
        total += abs(id - ids2[i])
    return total


def part2():
    total = 0
    counter1 = defaultdict(int)
    counter2 = defaultdict(int)
    for index in range(len(ids1)):
        counter1[ids1[index]] += 1
        counter2[ids2[index]] += 1
    for key, value in counter1.items():
        total += key*value*counter2.get(key, 0)
    return total


print(part1())
print(part2())
