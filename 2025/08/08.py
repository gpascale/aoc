import numpy as np

with open("./input.txt") as f:
    boxes = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

def part_a():
    grps = [i for i in range(len(boxes))]
    dists = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            d = sum([(boxes[i][k] - boxes[j][k]) ** 2 for k in range(3)])
            dists.append((d, i, j))
    dists = sorted(dists, key=lambda x: x[0])[:1000]
    for dist, i, j in dists[:1000]:
        old_grp = grps[j]
        new_grp = grps[i]
        for k in range(len(boxes)):
            if grps[k] == old_grp:
                grps[k] = new_grp
    unique, counts = np.unique(grps, return_counts=True)
    tups = sorted(list(zip(counts, unique)), reverse=True)
    print('Part A:', tups[0][0] * tups[1][0] * tups[2][0])

def part_b():
    grps = [i for i in range(len(boxes))]
    dists = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            d = sum([(boxes[i][k] - boxes[j][k]) ** 2 for k in range(3)])
            dists.append((d, i, j))
    dists = sorted(dists, key=lambda x: x[0])
    grpmem = [set([i]) for i in range(len(boxes))]
    for dist, i, j in dists:
        old_grp = grps[j]
        new_grp = grps[i]
        if old_grp == new_grp:
            continue
        for k in grpmem[old_grp]:
            grps[k] = new_grp
        grpmem[new_grp] = grpmem[new_grp].union(grpmem[old_grp])
        grpmem[old_grp] = set()
        if len(grpmem[new_grp]) == len(boxes):
            print('Part B:', boxes[i][0] * boxes[j][0])
            break


part_a()
part_b()