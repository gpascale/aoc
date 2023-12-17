import numpy as np
import heapq

moves = {'D': [0, 1], 'U': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
M = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
RM = 'UDLR'

def inbounds(x, y, G):
    return x >= 0 and y >= 0 and y < len(G) and x < len(G[0])

def solve(L, ma, mi):
    # state: (y, x, moves left, last direction)
    vis = np.zeros((len(L), len(L[0]), len(RM), ma - mi + 1), dtype=np.int32)
    sp = np.full((len(L), len(L[0]), len(RM), ma - mi + 1), 99999999, dtype=np.int32)
    q = ([(0, (0, 0, M['U'], 0)), (0, (0, 0, M['L'], 0))])
    sp[0, 0, M['U'], 0] = sp[0, 0, M['L'], 0] = 0
    while len(q):
        dist, state = heapq.heappop(q)
        vis[state] = 1
        x, y, di, left = state
        di = RM[di]
        try_dirs = [
            *([di] if left > 0 else []),
            *(['U', 'D'] if di in ['L', 'R'] else ['L', 'R'])
        ]
        for nd in try_dirs:
            mv = moves[nd]
            dist = 1 if nd == di else mi
            newpos = [x + (dist * mv[0]), y + (dist * mv[1])]
            if inbounds(newpos[0], newpos[1], G):
                mv = moves[nd]
                loss = np.sum([G[y + d * mv[1]][x + d * mv[0]] for d in range(1, dist + 1)])
                ns = (newpos[0], newpos[1], M[nd], left - 1 if nd == di else ma - mi)
                if not vis[ns] and sp[ns] > sp[state] + loss:
                    sp[ns] = sp[state] + loss
                    heapq.heappush(q, (sp[ns], ns))
    return np.min(sp[len(G) - 1, len(G[0]) - 1])

L = [s.strip() for s in open("./input.txt").readlines() if s]
G = [[int(c) for c in s] for s in L]

print('part 1:', solve(G, 3, 1))
print('part 2:', solve(G, 10, 4))
