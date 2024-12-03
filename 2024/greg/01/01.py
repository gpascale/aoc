import numpy as np


def part_a(path):
    a, b = np.int32([]), np.int32([])
    with open(path, "r") as f:
        for line in f:
            a = np.append(a, [int(line.split()[0])])
            b = np.append(b, [int(line.split()[1])])
    return np.sum(np.abs(np.sort(b) - np.sort(a)))


def part_b(path):
    a, b = np.int32([]), np.int32([])
    with open(path, "r") as f:
        for line in f:
            a = np.append(a, [int(line.split()[0])])
            b = np.append(b, [int(line.split()[1])])

    freq = {k: v for k, v in zip(*np.unique(b, return_counts=True))}
    return np.sum([a[i] * (freq[a[i]] if a[i] in freq else 0) for i in range(len(a))])


print("Example Input:")
print("Part A:", part_a("./input-example.txt"))
print("Part B:", part_b("./input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a("./input.txt"))
print("Part B:", part_b("./input.txt"))
