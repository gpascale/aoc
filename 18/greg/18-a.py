import numpy as np

right_turn = set(["RD", "DL", "LU", "UR"])
move = {"D": [0, 1], "U": [0, -1], "R": [1, 0], "L": [-1, 0]}
inside = {"D": [-1, 0], "U": [1, 0], "R": [0, 1], "L": [0, -1]}


def solve(S):
    turns = [str(f"{S[i][0]}{S[(i+1) % len(S)][0]}") for i in range(len(L))]
    print(turns)
    numR = len([1 for turn in turns if turn in right_turn])
    if numR < len(S) // 2:
        S = list(reversed(S))

    bounds = [[99999999, -99999999], [99999999, -99999999]]

    q = []
    G = np.zeros((5000000, 5000000), dtype=int)
    x = y = 5000
    for di, num_steps, color in S:
        num_steps = int(num_steps)
        print(di, num_steps, color)
        for _ in range(num_steps):
            G[y][x] = 2
            in_nb = (y + inside[di][1], x + inside[di][0])
            if G[in_nb] == 0:
                G[in_nb] = 1
                q.append((y + inside[di][1], x + inside[di][0]))
            y += move[di][1]
            x += move[di][0]
            bounds[0][0] = min(bounds[0][0], x)
            bounds[0][1] = max(bounds[0][1], x)
            bounds[1][0] = min(bounds[1][0], y)
            bounds[1][1] = max(bounds[1][1], y)

    G = G[bounds[1][0] : bounds[1][1] + 1, bounds[0][0] : bounds[0][1] + 1]
    q = [(c[0] - bounds[1][0], c[1] - bounds[0][0]) for c in q]
    print(q)

    vis = np.zeros((len(G), len(G[0])))
    while len(q):
        (y, x) = q.pop(0)
        if vis[y, x]:
            continue
        vis[y, x] = 1
        if G[y, x] == 0:
            G[y, x] = 1
        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if (
                x + d[0] >= 0
                and x + d[0] < len(G[0])
                and y + d[1] >= 0
                and y + d[1] < len(G)
                and G[y + d[1]][x + d[0]] == 0
            ):
                q.append((y + d[1], x + d[0]))
    return np.count_nonzero(G)


L = [s.strip() for s in open("./input.txt").readlines() if s]
steps = [s.replace("(", "").replace(")", "").split(" ") for s in L]
print(steps)

print("part 1:", solve(steps))
