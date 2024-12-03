import numpy as np
from collections import defaultdict


def disintegrate(supporting, supported_by):
    ret = 0
    for starter in range(len(supporting)):
        fallen = 0
        sup_by = [{*sup_set} for sup_set in supported_by]
        q = [starter]
        while len(q):
            b = q.pop(0)
            for y in supporting[b]:
                sup_by[y].remove(b)
                if len(sup_by[y]) == 0:
                    fallen += 1
                    q.append(y)
        ret += fallen
    print('part 2:', ret)


def solve(bricks):
    bricks.sort(key=lambda b: b['z'])
    heights = np.zeros((10, 10), dtype='int')
    highest = np.zeros((10, 10), dtype='int')
    highest.fill(-1)
    supporting = [set() for i in range(len(bricks))]
    supported_by = [set() for i in range(len(bricks))]
    for i in range(len(bricks)):
        pos, h, z = (bricks[i]['pos'], bricks[i]['h'], bricks[i]['z'])
        restingH = 0
        supporters = set()
        for x in range(pos['x'], pos['x'] + pos['w']):
            for y in range(pos['y'], pos['y'] + pos['l']):
                if heights[x, y] > restingH:
                    restingH = heights[x, y]
                    supporters = set()
                if heights[x, y] == restingH and highest[x, y] >= 0:
                    supporters.add(highest[x, y])
        for x in range(pos['x'], pos['x'] + pos['w']):
            for y in range(pos['y'], pos['y'] + pos['l']):
                heights[x, y] = restingH + h
                highest[x, y] = i
        for s in supporters:
            supporting[s].add(i)
            supported_by[i].add(s)

    cant_remove = set()
    for i in range(len(bricks)):
        if len(supported_by[i]) == 1:
            cant_remove.add(list(supported_by[i])[0])
    print('part 1:', len(bricks) - len(cant_remove))

    disintegrate(supporting, supported_by)


bricks = []
L = [l.strip() for l in open("./input.txt").readlines() if l.strip() != '']
for l in L:
    [s, e] = [[*map(int, s.split(','))] for s in l.split('~')]
    bricks.append({'pos': {'x': s[0], 'y': s[1], 'w': e[0] - s[0] + 1,
                  'l': e[1] - s[1] + 1}, 'h': e[2] - s[2] + 1, 'z': start[2]})
solve(bricks)
