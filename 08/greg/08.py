import re
import numpy as np
import sys
import math

sys.setrecursionlimit(100000)


def build_nodes():
    nodes = {}
    for line in [l for l in lines[1:] if l]:
        [src, l, r] = re.findall(r"[0-9A-Z]{3}", line)
        nodes[src] = [l, r]
    return nodes


def solve_part_1(lines):
    steps = ["LR".index(c) for c in lines[0]]
    nodes = build_nodes()
    step = 0
    ret = 0
    cur = "AAA"
    while cur != "ZZZ":
        cur = nodes[cur][steps[step]]
        step = (step + 1) % len(steps)
        ret += 1
    print("part 1:", ret)


def walk_to_z(node, step):
    global nodes
    global steps
    global z_nodes
    global state
    if state[node][step] != (-1, -1):
        return state[node][step]
    else:
        next_node = nodes[node][steps[step]]
        if next_node in z_nodes:
            state[node][step] = [1, next_node]
            return state[node][step]

        # mark state as visited
        state[node][step] = [-2, -2]
        [num_steps, z_node] = walk_to_z(next_node, (step + 1 + len(steps)) % len(steps))
        if num_steps == -2:
            # found a cycle
            state[node][step] = [-2, -2]
        else:
            assert num_steps != -1
            state[node][step] = [1 + num_steps, z_node]
    return state[node][step]


def solve_part_2(lines):
    global nodes
    global steps
    global z_nodes
    global state
    steps = ["LR".index(c) for c in lines[0]]
    nodes = build_nodes()

    ordered_nodes = sorted(nodes.keys())
    node_idx = {k: i for i, k in enumerate(ordered_nodes)}
    a_nodes = set([i for i, k in enumerate(ordered_nodes) if k.endswith("A")])
    z_nodes = set([i for i, k in enumerate(ordered_nodes) if k.endswith("Z")])
    nodes = [[node_idx[nodes[k][0]], node_idx[nodes[k][1]]] for k in ordered_nodes]
    state = [[(-1, -1) for _ in range(len(steps))] for __ in range(len(ordered_nodes))]
    for i in range(len(ordered_nodes)):
        for j in range(len(steps)):
            walk_to_z(i, j)

    ret = 0
    cur_step = 0
    cur = [state[node][cur_step] for node in a_nodes]

    # OH MY GOD FUCK YOU ADVENT OF CODE - THIS IS SOME BULLSHIT
    print("part 2:", math.lcm(*[c[0] for c in cur]))
    return

    # while 1:
    #     print("iter", iterations, "cs", cur_step, "ret", ret)
    #     iterations += 1
    #     # print(cur_step, cur)
    #     if len(set([c[0] for c in cur])) == 1:
    #         ret = ret + cur[0][0]
    #         break
    #     steps_to_take = min([c[0] for c in cur])
    #     # print("stt", steps_to_take)
    #     ret = ret + steps_to_take
    #     cur_step = (cur_step + steps_to_take + len(steps)) % len(steps)
    #     # print("cs", cur_step)
    #     for i in range(len(cur)):
    #         assert cur[i][0] != -2
    #         if cur[i][0] == steps_to_take:
    #             cur[i] = state[cur[i][1]][cur_step]
    #         else:
    #             cur[i] = (cur[i][0] - steps_to_take, cur[i][1])

    # print("ret", ret)


lines = [s.strip() for s in open("./input.txt").readlines() if s]
solve_part_1(lines)
solve_part_2(lines)
