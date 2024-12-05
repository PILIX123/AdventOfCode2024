lines: list[str]
with open("inputs/day2.txt") as f:
    lines = f.readlines()


reportList: list[list[int]] = []
for line in lines:
    split = line.split(" ")
    reportList.append([int(s) for s in split])


def partOne():
    total = 0
    for report in reportList:

        ascending = False
        descending = False
        for i, v in enumerate(report):
            if i == 0:
                continue
            if report[i-1] < v:
                ascending = True
            if report[i-1] > v:
                descending = True
            if ascending and descending:
                break
            if not (0 < abs(v-report[i-1]) and abs(v-report[i-1]) <= 3):
                break
            if i+1 == len(report):
                total += 1
    return total


def partTwo():
    total = 0
    for report in reportList:
        ascending = False
        descending = False
        single = False
        for i, v in enumerate(report):
            if i == 0:
                continue
            current = (ascending, descending)
            if report[i-1] < v:
                ascending = True
            if report[i-1] > v:
                descending = True
            if ascending and descending:
                if single:
                    break
                report.pop(i)
                # figure it out
                if not (check(report)):
                    break

            if not (0 < abs(v-report[i-1]) and abs(v-report[i-1]) <= 3):
                if single:
                    break
                report.pop(i)
                if not (check(report)):
                    break
                break
            if i+1 == len(report):
                total += 1
    return total


print(partOne())
print(partTwo())
