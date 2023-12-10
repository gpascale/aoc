import numpy as np
import sys

sys.setrecursionlimit(100000)

start_x = -1
start_y = -1

grid = [s.strip() for s in open("./input.txt").readlines() if s]
for row in range(len(grid)):
    grid[row] = [c for c in grid[row]]
    if 'S' in grid[row]:
        start_x = grid[row].index('S')
        start_y = row

dirs = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}
moves = {
    "L-": "L", "R-": "R",
    "U|": "U", "D|": "D",
    "R7": "D", "U7": "L",
    "LF": "D", "UF": "R",
    "DJ": "L", "RJ": "U",
    "LL": "U", "DL": "R",
}


def dfs(x, y, prev_dir, num_steps):
    global start_x, start_y
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return -1
    if x == start_x and y == start_y and num_steps > 0:
        return num_steps // 2
    key = f"{prev_dir}{grid[y][x]}"
    dir = moves[key]
    nx = x + dirs[dir][0]
    ny = y + dirs[dir][1]
    next_key = f"{dir}{grid[ny][nx]}"
    if next_key not in moves:
        return -1
    return dfs(nx, ny, dir, num_steps + 1)


def solve_part_1():
    global start_x, start_y
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start_x = x
                start_y = y
                for move in moves:
                    grid[y][x] = move[1]
                    ret = dfs(x, y, move[0], 0)
                    if ret != -1:
                        print("part 1:", ret)
                        return


solve_part_1()
