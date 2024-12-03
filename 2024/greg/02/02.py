import numpy as np
import os

root = os.path.dirname(os.path.realpath(__file__))


def part_a(path):
    with open(path, "r") as f:
        reports = [np.int32([int(x) for x in line.split()]) for line in f]
    diffs = [np.diff(l) for l in reports]
    sign_good = np.array([len(np.unique(np.sign(l))) == 1 for l in diffs])
    diff_good = np.array([np.max(np.abs(l)) <= 3 and np.all(l != 0) for l in diffs])
    return np.sum(sign_good & diff_good)


def part_b(path):
    with open(path, "r") as f:
        reports = [np.int32([int(x) for x in line.split()]) for line in f]
    num_good = 0
    for report in reports:
        perms = [report]
        for i in range(len(report)):
            perms.append(np.append(report[:i], report[(i + 1) :]))
        for perm in perms:
            diff = np.diff(perm)
            sign_good = len(np.unique(np.sign(diff))) == 1
            diff_good = np.max(np.abs(diff)) <= 3 and np.all(diff != 0)
            if sign_good and diff_good:
                num_good += 1
                break
    return num_good


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
