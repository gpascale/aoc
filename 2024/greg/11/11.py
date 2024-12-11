import os
import numpy as np
from collections import defaultdict

root = os.path.dirname(os.path.realpath(__file__))


def blink(stone):
    if stone == 0:
        return [1]
    ndig = len(str(stone))
    if ndig % 2 == 0:
        return [int(str(stone)[: ndig // 2]), int(str(stone)[ndig // 2 :])]
    else:
        return [stone * 2024]


def part_a(path):
    with open(path, "r") as f:
        stones = [s.strip() for s in f.readlines()][0]
    stones = [int(c) for c in stones.split(" ")]
    for _ in range(0, 25):
        stones = [c for sublist in [blink(c) for c in stones] for c in sublist]
    return len(stones)


def part_b(path):
    with open(path, "r") as f:
        stones = [s.strip() for s in f.readlines()][0]
    stones = {int(c): 1 for c in stones.split(" ")}
    for _ in range(0, 75):
        newstones = defaultdict(int)
        for stone, cnt in stones.items():
            stone_counts = dict(zip(*np.unique(blink(stone), return_counts=True)))
            for k, v in stone_counts.items():
                newstones[k] += v * cnt
        stones = newstones
    return sum(stones.values())


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
