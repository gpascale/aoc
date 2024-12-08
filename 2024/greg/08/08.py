import os
import math
from collections import defaultdict

root = os.path.dirname(os.path.realpath(__file__))

def in_bounds(grid, x, y):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def part_a(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    locs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                locs[grid[i][j]].append((j, i))
    locs = { k: v for k, v in locs.items() if len(v) > 1 }
    ret = set()
    for _, v in locs.items():
        # print(_, v)
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                x0, y0 = v[i]
                x1, y1 = v[j]
                d = (x1 - x0), (y1 - y0)
                a1 = (x0 - d[0], y0 - d[1])
                a2 = (x1 + d[0], y1 + d[1])
                if in_bounds(grid, *a1):
                    ret.add(a1)
                if in_bounds(grid, *a2):
                    ret.add(a2)
    return len(ret)

def part_b(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    locs = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                locs[grid[i][j]].append((j, i))
    locs = { k: v for k, v in locs.items() if len(v) > 1 }
    ret = set()
    for _, v in locs.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                x0, y0 = v[i]
                x1, y1 = v[j]
                d = (x1 - x0), (y1 - y0)
                g = math.gcd(abs(x1 - x0), abs(y1 - y0))
                d = d[0] // g, d[1] // g
                ret.add((x0, y0))
                for dx, dy in [(d[0], d[1]), (-d[0], -d[1])]:
                    x, y = x0, y0
                    while True:
                        x, y = x + dx, y + dy
                        if not in_bounds(grid, x, y):
                            break
                        ret.add((x, y))
    return len(ret)


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
