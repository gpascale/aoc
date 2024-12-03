import re
import numpy as np
import sys
import random

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


def dfs(x, y, prev_dir, loop_tiles):
    global start_x, start_y
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return []
    if x == start_x and y == start_y and len(loop_tiles) > 0:
        return loop_tiles
    key = f"{prev_dir}{grid[y][x]}"
    dir = moves[key]
    nx = x + dirs[dir][0]
    ny = y + dirs[dir][1]
    next_key = f"{dir}{grid[ny][nx]}"
    if next_key not in moves:
        return []
    return dfs(nx, ny, dir, [*loop_tiles, (x, y)])


def find_loop():
    global start_x, start_y
    for move in moves:
        grid[start_y][start_x] = move[1]
        loop = dfs(start_x, start_y, move[0], [])
        if len(loop) > 0:
            return loop


def solve_part_2():
    loop = set(find_loop())
    ret = 0

    for y in range(len(grid)):
        is_inside = 0
        ang_open = None
        for x in range(len(grid[0])):
            if (x, y) in loop:
                if grid[y][x] == "|":
                    is_inside = 1 - is_inside
                elif grid[y][x] in "FL":
                    ang_open = grid[y][x]
                elif grid[y][x] in "J7":
                    assert ang_open is not None
                    if f'{ang_open}{grid[y][x]}' in ['FJ', 'L7']:
                        is_inside = 1 - is_inside
                        ang_open = None
            else:
                if is_inside:
                    ret += 1

    print("part 2:", ret)


solve_part_2()
