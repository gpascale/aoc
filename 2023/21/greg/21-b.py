import numpy as np


def sq(x):
    return x * x


def solve(G, r, c):
    ret = 0
    q = [(r, c, 0, 0, 0)]
    sp = np.zeros((len(G), len(G[0]), 5, 5), dtype=np.int32)
    while len(q):
        r, c, wr, wc, d = q.pop(0)
        if G[r, c] == 0:
            continue
        if sp[r, c, wr + 2, wc + 2] != 0:
            continue
        sp[r, c, wr + 2, wc + 2] = d
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            nwr = (wr + 1 if nr >= len(G) else wr - 1 if nr < 0 else wr)
            nwc = (wc + 1 if nc >= len(G[0]) else wc - 1 if nc < 0 else wc)
            nr = (nr + len(G)) % len(G)
            nc = (nc + len(G[0])) % len(G[0])
            if G[nr, nc] == 0:
                continue
            if abs(nwr) > 2 or abs(nwc) > 2:
                continue
            if sp[nr, nc, nwr + 2, nwc + 2] != 0:
                continue
            q.append((nr, nc, nwr, nwc, d + 1))

    max_moves = 26501365

    for r in range(len(G)):
        for c in range(len(G[0])):
            if sp[r, c, 0 + 2, 0 + 2] != 0:
                onmod = (r + c + 2) % 2 == max_moves % 2
                ret += 1 if onmod else 0
                ri = 1 + ((max_moves - sp[r, c, 0 + 2, 1 + 2]) // len(G))
                le = 1 + ((max_moves - sp[r, c, 0 + 2, -1 + 2]) // len(G))
                u = 1 + ((max_moves - sp[r, c, -1 + 2, 0 + 2]) // len(G))
                d = 1 + ((max_moves - sp[r, c, 1 + 2, 0 + 2]) // len(G))
                ur = 1 + (((max_moves - sp[r, c, -1 + 2, 1 + 2]) // len(G)))
                ul = 1 + (((max_moves - sp[r, c, -1 + 2, -1 + 2]) // len(G)))
                dr = 1 + (((max_moves - sp[r, c, 1 + 2, 1 + 2]) // len(G)))
                dl = 1 + (((max_moves - sp[r, c, 1 + 2, -1 + 2]) // len(G)))
                if onmod:
                    ri = (ri + 0) // 2
                    le = (le + 0) // 2
                    u = (u + 0) // 2
                    d = (d + 0) // 2
                    ur = sq((ur + 1) // 2)
                    ul = sq((ul + 1) // 2)
                    dr = sq((dr + 1) // 2)
                    dl = sq((dl + 1) // 2)
                else:
                    ri = (ri + 1) // 2
                    le = (le + 1) // 2
                    u = (u + 1) // 2
                    d = (d + 1) // 2
                    ur = sq(ur // 2) + (ur // 2)
                    ul = sq(ul // 2) + (ul // 2)
                    dr = sq(dr // 2) + (dr // 2)
                    dl = sq(dl // 2) + (dl // 2)
                ret += ri + le + u + d + ur + ul + dr + dl
    return ret


cmap = {'#': 0, '.': 1, 'S': 2}
with open("./input.txt") as f:
    G = np.array([[cmap[c] for c in l.strip()] for l in f.readlines()])
r, c = [x[0] for x in np.where(G == 2)]
G[r, c] = 1
print(solve(G, r, c))

# print distances

# for r in range(len(G)):
#     for c in range(len(G[0])):
#         if sp[r, c, 0 + 2, 50] != 0:
#             print(r, c)
#             print('onmod:', (r + c + 2) % 2 == max_moves % 2)
#             for dr in range(-3, 4):
#                 print([sp[r, c, 50 + dr, 50 + dc]
#                         for dc in range(-5, 6)])
