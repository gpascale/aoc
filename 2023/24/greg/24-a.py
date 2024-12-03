import numpy as np

MIN = 200000000000000
MAX = 400000000000000


def intersect(p1, v1, p2, v2, min=MIN, max=MAX):
    p1_m = v1[1] / v1[0]
    p2_m = v2[1] / v2[0]
    p1_b = p1[1] + (0 - p1[0]) * v1[1] / v1[0]
    p2_b = p2[1] + (0 - p2[0]) * v2[1] / v2[0]
    if p1_m == p2_m:
        return 0
    x_int = (p2_b - p1_b) / (p1_m - p2_m)
    y_int = p1_m * x_int + p1_b
    if MIN <= x_int <= MAX and MIN <= y_int <= MAX:
        p1_head = (v1[0] > 0) == ((x_int - p1[0]) > 0)
        p2_head = (v2[0] > 0) == ((x_int - p2[0]) > 0)
        return 1 if (p1_head and p2_head) else 0
    return 0


def solve(P):
    ret = 0
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            ret += intersect(P[i][0], P[i][1], P[j][0], P[j][1])
    return ret


L = [l.strip() for l in open("./input.txt").readlines()]
P = []
for l in L:
    P.append(tuple([[*map(int, s.strip().split(","))] for s in l.split("@")]))
print("part 1:", solve(P))
