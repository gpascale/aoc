import os
from collections import deque

root = os.path.dirname(os.path.realpath(__file__))

def in_bounds(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def part_a(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    plot = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    ret = 0
    nextplot = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if plot[i][j] == -1:
                perim, area = (0, 0)
                q = deque([(i, j)])
                while len(q) > 0:
                    r, c = q.popleft()
                    if plot[r][c] != -1:
                        continue
                    plot[r][c] = nextplot
                    area += 1
                    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        nr, nc = r + dr, c + dc
                        if in_bounds(nr, nc, grid) and grid[nr][nc] == grid[r][c]:
                            q.append((nr, nc))
                        else:
                            perim += 1
                nextplot += 1
                ret += area * perim
    return ret

def is_side(r, c, dr, dc, grid):
    return not in_bounds(r + dr, c + dc, grid) or grid[r + dr][c + dc] != grid[r][c]

def part_b(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    plot = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    nextplot = 0
    ret = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if plot[i][j] == -1:
                area = 0
                minr, minc, maxr, maxc = (i, j, i+1, j+1)
                q = deque([(i, j)])
                # identify the plot
                while len(q) > 0:
                    r, c = q.popleft()
                    if plot[r][c] != -1:
                        continue
                    minr, minc = min(r, minr), min(c, minc)
                    maxr, maxc = max(r + 1, maxr), max(c + 1, maxc)
                    plot[r][c] = nextplot
                    area += 1
                    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        nr, nc = r + dr, c + dc
                        if in_bounds(nr, nc, grid) and grid[nr][nc] == grid[r][c]:
                            q.append((nr, nc))
                # count sides
                sides = 0
                for r in range(minr, maxr):
                    topside, bottomside = 0, 0
                    for c in range(minc, maxc):
                        if plot[r][c] != nextplot:
                            topside, bottomside = 0, 0
                            continue
                        if is_side(r, c, -1, 0, plot):
                            sides += 1 - topside
                            topside = 1
                        else:
                            topside = 0
                        if is_side(r, c, 1, 0, plot):
                            sides += 1 - bottomside
                            bottomside = 1
                        else:
                            bottomside = False
                for c in range(minc, maxc):
                    leftside, rightside = 0, 0
                    for r in range(minr, maxr):
                        if plot[r][c] != nextplot:
                            leftside, rightside = 0, 0
                            continue
                        if is_side(r, c, 0, -1, plot):
                            sides += 1 - leftside
                            leftside = 1
                        else:
                            leftside = 0
                        if is_side(r, c, 0, 1, plot):
                            sides += 1 - rightside
                            rightside = 1
                        else:
                            rightside = 0
                ret += area * sides
                nextplot += 1

    return ret

print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
