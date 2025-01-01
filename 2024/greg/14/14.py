import os
import math
import numpy as np

root = os.path.dirname(os.path.realpath(__file__))

def part_a(path, W=101, H=103):
    with open(path, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    p, v = [], []
    for line in lines:
        pp, vv = [[int(c) for c in x[2:].split(',')] for x in line.split()]
        p.append(pp)
        v.append(vv)
    for i in range(len(p)):
        p[i] = [(100 * v[i][0] + p[i][0]) % W, (100 * v[i][1] + p[i][1]) % H]
    quads = np.zeros((2, 2), dtype=int)
    p = [x for x in p if x[0] != (W // 2) and x[1] != (H // 2)]
    print(p)
    for i in range(len(p)):
        quads[int(p[i][0] > (W // 2)), int(p[i][1] > (H // 2))] += 1
    ret = np.multiply(*np.multiply(*quads))
    return ret

def part_b(path, W=101, H=103):
    with open(path, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    p, v = [], []
    for line in lines:
        pp, vv = [[int(c) for c in x[2:].split(',')] for x in line.split()]
        p.append(pp)
        v.append(vv)
    with open("output.txt", "w") as f:
        for s in range(20000):
            for i in range(len(p)):
                p[i] = [((100 * W) + v[i][0] + p[i][0]) % W, ((100 * H) + v[i][1] + p[i][1]) % H]
            cnt = sum([1 for x in p if 20 <= x[0] <= 50])
            if cnt > 300:
                lines = [['.' for _ in range(W)] for _ in range(H)]
                for i in range(len(p)):
                    lines[p[i][1]][p[i][0]] = '#'
                print('\n', file=f)
                print(f'{s} seconds:', file=f)
                for line in lines:
                    print(''.join(line), file=f)
    return 'N/A'

print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt", 11, 7))
# print("Part B:", part_b(f"{root}/input-example.txt", 11, 7))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
