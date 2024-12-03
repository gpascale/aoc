import numpy as np
import sys
from collections import defaultdict


L = [l.strip() for l in open("./input.txt").readlines()]
P = []
for l in L:
    P.append([[*map(int, s.strip().split(","))] for s in l.split("@")])


def intersect(p1, v1, p2, v2):
    [x1, y1, vx1, vy1, x2, y2, vx2, vy2] = [*p1, *v1, *p2, *v2]
    det = vx1 * vy2 - vy1 * vx2
    if det == 0:
        raise Exception("parallel")
    t = ((x2 - x1) * vy2 - (y2 - y1) * vx2) / det
    s = ((x2 - x1) * vy1 - (y2 - y1) * vx1) / det
    return ([x1 + t * vx1, y1 + t * vy1], t, s)


def poss_velos(d, v, candidates=None):
    ret = set()
    d = abs(d)
    if candidates is None:
        candidates = range(-1, int(np.sqrt(abs(d))) + 1)
    for c in candidates:
        for rel_v in [abs(v + c), abs(v - c)]:
            if d != 0 and rel_v != 0 and d % rel_v == 0:
                ret.add(abs(c))
    return ret


# find the velocity by considering pairs of particles which
# have the same x, y, or z coordinate - only certain values
# will divide the distance between them integer...ly
by_cmp = {k: defaultdict(list) for k in "xyz"}
for i in range(len(P)):
    for dim in range(3):
        by_cmp["xyz"[dim]][i][P[i][1][dim]].append(i)
candidates = {"x": None, "y": None, "z": None}
for dim in "xyz":
    for k in by_cmp[dim]:
        if len(by_cmp[dim][k]) > 1:
            for i in range(len(by_cmp[dim][k])):
                for j in range(i + 1, len(by_cmp[dim][k])):
                    ii = by_cmp[dim][k][i]
                    jj = by_cmp[dim][k][j]
                    diff = P[ii][0]["xyz".index(dim)] - P[jj][0]["xyz".index(dim)]
                    candidates[dim] = poss_velos(diff, k, candidates[dim])

# make sure we've reduced the candidates to a single possibility
assert all([len(candidates[dim]) == 1 for dim in "xyz"])
v = np.array([list(candidates[dim])[0] for dim in "xyz"]).flatten()
print("vel:", v)

p_0, v_0, p_1, v_1 = [np.array(x) for x in [P[0][0], P[0][1], P[1][0], P[1][1]]]

for mul in [
    np.array([1, 1, 1]),
    np.array([1, 1, -1]),
    np.array([1, -1, 1]),
    np.array([1, -1, -1]),
    np.array([-1, 1, 1]),
    np.array([-1, 1, -1]),
    np.array([-1, -1, 1]),
    np.array([-1, -1, -1]),
]:
    v_0_rel = v_0 - (mul * v)
    v_1_rel = v_1 - (mul * v)

    isect_pt, t, s = intersect(p_0[:2], v_0_rel[:2], p_1[:2], v_1_rel[:2])
    if t == int(t) and s == int(s):
        c = p_0 + (v_0_rel * t)
        print("ctr:", c.astype(int))
        print("answer:", int(c.sum()))
        break
