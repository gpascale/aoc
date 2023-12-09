import re
import numpy as np

example_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def solve_part_1(lines):
    rows = [np.array([int(x) for x in line.split(" ")]) for line in lines]
    ret = 0
    for a in rows:
        while len(a) > 1:
            ret = ret + a[-1]
            if len(set(a)) == 1:
                break
            a = np.diff(a)
    print("part 1:", ret)


def solve_part_2(lines):
    rows = [np.array([int(x) for x in line.split(" ")]) for line in lines]
    ret = 0
    for a in rows:
        for r in range(0, len(a) - 1):
            ret += a[0] if r % 2 == 0 else -a[0]
            if len(set(a)) == 1:
                break
            a = np.diff(a)
    print("part 2:", ret)


example_lines = [s.strip() for s in example_input.split("\n") if s]
lines = [s.strip() for s in open("./input.txt").readlines() if s]
solve_part_1(lines)
solve_part_2(lines)
