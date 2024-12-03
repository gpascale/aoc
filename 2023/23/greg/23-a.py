import numpy as np
import sys

sys.setrecursionlimit(100000)

dirs = {
    ">": [[0, 1]],
    "<": [[0, -1]],
    "^": [[-1, 0]],
    "v": [[1, 0]],
    ".": [[0, 1], [0, -1], [-1, 0], [1, 0]],
}

vis = None
lp = None
best_lp = None


def dfs(G, r, c, dist):
    global lp
    global best_lp
    best_lp[r, c] = max(best_lp[r, c], dist)
    ret = {}
    for d in dirs[G[r][c]]:
        nr = r + d[0]
        nc = c + d[1]
        if nr < 0 or nc < 0 or nr >= len(G) or nc >= len(G[0]):
            continue
        if G[nr][nc] == "#":
            continue
        next_is_slope = G[nr][nc] in ["^", "v", "<", ">"]
        if (
            next_is_slope
            and nr + dirs[G[nr][nc]][0][0] == r
            and nc + dirs[G[nr][nc]][0][1] == c
        ):
            continue
        is_slope = G[r][c] in ["^", "v", "<", ">"]
        if is_slope:
            if (nr, nc) not in ret:
                ret[(nr, nc)] = dist + 1
            else:
                ret[(nr, nc)] = max(ret[(nr, nc)], dist + 1)
        else:
            if lp[nr, nc] >= 0:
                continue
            lp[nr, nc] = dist + 1
            ret = {**ret, **dfs(G, nr, nc, dist + 1)}
            lp[nr, nc] = -1
    return ret


def solve(G):
    global lp
    global best_lp
    lp = np.zeros((len(G), len(G[0])), dtype=np.int32)
    best_lp = np.zeros((len(G), len(G[0])), dtype=np.int32)
    lp.fill(-1)
    best_lp.fill(-1)
    q = [(1, 1, 0)]
    while len(q):
        r, c, dist = q.pop(0)
        lp[r, c] = dist
        ret = dfs(G, r, c, dist)
        for (r, c), v in ret.items():
            q.append((r, c, v))

    return best_lp[(len(G) - 2, len(G[0]) - 2)]


G = [l.strip() for l in open("./input.txt").readlines()]
print("part 1:", solve(G))
