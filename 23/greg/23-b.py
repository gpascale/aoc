import numpy as np
import sys
import re
from collections import defaultdict

sys.setrecursionlimit(100000)

G = [l.strip() for l in open("./input.txt").readlines()]
G = [re.sub(r"[<^>v]", ".", l) for l in G]
SRC = (1, 1)
DST = (len(G) - 2, len(G[0]) - 2)
W = len(G[0])
H = len(G)


# return manhattan neighbors (U, D, L, R) for a given square
def mnh_nbrs(r, c):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(r + dr, c + dc) for dr, dc in d if 0 <= r + dr < H and 0 <= c + dc < W]


def walk_edges(edge_squares, node_squares):
    edges = []
    while len(edge_squares):
        q = [list(edge_squares)[0]]
        dist = 0
        endpoints = []
        while len(q):
            r, c = q.pop(0)
            edge_squares.remove((r, c))
            dist += 1
            for nr, nc in mnh_nbrs(r, c):
                if (nr, nc) in edge_squares:
                    q.append((nr, nc))
                elif (nr, nc) in node_squares:
                    endpoints.append((nr, nc))
        if len(endpoints) == 2:
            edges.append((endpoints[0], endpoints[1], dist))
    return edges


# build a simplified graph by collapsing long branch-less paths
# and removing dead-ends
def build_graph():
    node_squares = set()
    edge_squares = set()
    for r, c in [s for s in np.ndindex(H, W) if G[s[0]][s[1]] != "#"]:
        if G[r][c] == "#":
            continue
        nbr_cnt = len([1 for nr, nc in mnh_nbrs(r, c) if G[nr][nc] != "#"])
        if nbr_cnt > 2:
            node_squares.add((r, c))
        else:
            edge_squares.add((r, c))

    # walk edges to create pairs of connected nodes
    edges = walk_edges(edge_squares, node_squares)
    graph = defaultdict(list)
    for src_node, dst_node, distance in edges:
        graph[src_node].append((dst_node, distance))
        graph[dst_node].append((src_node, distance))
    return graph


# recursively explore paths from start to end node, saving longest
def solve(src, dst):
    graph = build_graph()

    vis = {k: 0 for k in graph.keys()}
    lp = {k: 0 for k in graph.keys()}

    def _solve_recursive(cur, distance):
        vis[cur] = 1
        lp[cur] = max(lp[cur], distance)
        if cur == dst:
            return

        for next_node, d in graph[cur]:
            if vis[next_node] == 1:
                continue
            vis[next_node] = 1
            _solve_recursive(next_node, distance + d + 1)
            vis[next_node] = 0

    _solve_recursive(src, 0)
    return lp[DST]


print("part 2:", solve(SRC, DST))
