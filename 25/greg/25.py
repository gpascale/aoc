import sys
import random
import numpy as np
from collections import defaultdict

sys.setrecursionlimit(10000)

G = defaultdict(list)

lines = [l.strip() for l in open("./input.txt").readlines()]
for line in lines:
    line = line.strip()
    [from_node, to_nodes] = [line.split(":")[0], line.split(":")[1].strip().split(" ")]
    for to_node in to_nodes:
        G[from_node].append(to_node)
        G[to_node].append(from_node)


# do a BFS from start to end and return the path
def walk_path(start, end):
    prev = {}
    q = [start]
    while len(q) > 0 and end not in prev:
        cur = q.pop(0)
        for nxt in G[cur]:
            if nxt not in prev:
                prev[nxt] = cur
                q.append(nxt)
    if not end in prev:
        # no path found
        return None
    # reconstruct the path
    cur = end
    ret = []
    while cur != start:
        ret.append(tuple(sorted([prev[cur], cur])))
        cur = prev[cur]
    return ret


for iteration in range(3):
    tot = defaultdict(int)
    for trial in range(10000):
        start = random.choice([*G.keys()])
        end = random.choice([*G.keys()])
        if start == end or end in G[start]:
            continue
        path = walk_path(start, end)
        for edge in path:
            tot[edge] += 1

    # remove the most visited edge
    items = [(i[1], i[0]) for i in tot.items()]
    items.sort()
    remove_edge = items[-1][1]
    G[remove_edge[0]].remove(remove_edge[1])
    G[remove_edge[1]].remove(remove_edge[0])


# do a BFS from start and return the number of nodes visited
def bfs_count(start):
    vis = set()
    q = [start]
    while len(q):
        cur = q.pop(0)
        vis.add(cur)
        for nxt in G[cur]:
            if nxt not in vis:
                q.append(nxt)
    return len(vis)


size = set()
for trial in range(100):
    size.add(bfs_count(random.choice([*G.keys()])))
print(np.prod([*size]))
