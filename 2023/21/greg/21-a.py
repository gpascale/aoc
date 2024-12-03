import numpy as np


def solve(G, r, c):
    ret = 1
    q = [(r, c, 64)]
    mod = (r + c + 2) % 2
    vis = np.zeros((len(G), len(G[0])), dtype=np.int32)
    while len(q):
        r, c, d = q.pop(0)
        if r < 0 or c < 0 or r >= len(G) or c >= len(G[0]):
            continue
        if vis[r, c] == 1:
            continue
        vis[r, c] = 1
        if G[r, c] == 0:
            continue
        if G[r, c] == 1 and (r + c + 2) % 2 == mod:
            ret += 1
        if d > 0:
            q.append((r + 1, c, d - 1))
            q.append((r - 1, c, d - 1))
            q.append((r, c + 1, d - 1))
            q.append((r, c - 1, d - 1))
    return ret


cmap = {'#': 0, '.': 1, 'S': 2}
with open("./input.txt") as f:
    G = np.array([[cmap[c] for c in l.strip()] for l in f.readlines()])
r, c = [x[0] for x in np.where(G == 2)]
print(solve(G, r, c))
