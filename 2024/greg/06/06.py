import os
import numpy as np
from collections import defaultdict

root = os.path.dirname(os.path.realpath(__file__))


def in_bounds(x, y, W, H):
    return x >= 0 and x < W and y >= 0 and y < H


def part_a(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    W, H = len(grid[0]), len(grid)
    x, y = -1, -1
    for i in range(len(grid)):
        if "^" in grid[i]:
            x, y = grid[i].index("^"), i
            break
    d = (0, -1)
    vis = set()
    while True:
        vis.add((x, y))
        if not in_bounds(x + d[0], y + d[1], W, H):
            break
        if grid[y + d[1]][x + d[0]] == "#":
            d = (-d[1], d[0])
        x, y = x + d[0], y + d[1]
    return len(vis)


def part_b(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    W, H = len(grid[0]), len(grid)
    x_start, y_start = -1, -1
    for i in range(len(grid)):
        if "^" in grid[i]:
            x_start, y_start = grid[i].index("^"), i
            break
    ret = 0

    candidates = set()
    x, y = x_start, y_start
    d = (0, -1)
    while True:
        # print(x, y)
        if not in_bounds(x, y, W, H):
            break
        if x != x_start or y != y_start:
            candidates.add((x, y))
        if not in_bounds(x + d[0], y + d[1], W, H):
            break
        if grid[y + d[1]][x + d[0]] != "#":
            x, y = x + d[0], y + d[1]
        elif grid[y + d[1]][x + d[0]] == "#":
            d = (-d[1], d[0])

    for cx, cy in candidates:
        grid[cy] = grid[cy][:cx] + "#" + grid[cy][cx + 1 :]
        d = (0, -1)
        x, y = x_start, y_start
        vis = set()
        is_cycle = False
        while True:
            if not in_bounds(x, y, W, H):
                break
            if (x, y, d[0], d[1]) in vis:
                is_cycle = True
                break
            vis.add((x, y, d[0], d[1]))
            if not in_bounds(x + d[0], y + d[1], W, H):
                break
            if grid[y + d[1]][x + d[0]] != "#":
                x, y = x + d[0], y + d[1]
            else:
                d = (-d[1], d[0])
        grid[cy] = grid[cy][:cx] + "." + grid[cy][cx + 1 :]
        if is_cycle:
            ret += 1
    return ret


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
