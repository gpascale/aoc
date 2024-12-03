import numpy as np
import math
import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

rules = {}
state = {}


hit_ll = defaultdict(list)


def press(i):
    q = []
    for dst in rules["broadcaster"][1]:
        q.append(("broadcaster", dst, 0))

    while len(q) > 0:
        from_rule, to_rule, val = q.pop(0)
        if to_rule == "ll" and val == 1:
            hit_ll[from_rule].append(i + 1)
        if not to_rule in rules:
            continue

        # update state
        newval = val
        if rules[to_rule][0] == "%":
            if val != 0:
                continue
            state[to_rule]["on"] = 1 - state[to_rule]["on"]
            newval = state[to_rule]["on"]
        elif rules[to_rule][0] == "&":
            if val != state[to_rule]["recent"][from_rule]:
                state[to_rule]["recent"][from_rule] = val
            newval = (
                0 if all([x == 1 for x in state[to_rule]["recent"].values()]) else 1
            )

        # propagate
        for dst in rules[to_rule][1]:
            q.append((to_rule, dst, newval))


def parse_rules(R):
    rules = {}
    for s in R:
        tp = "b"
        parts = s.split(" -> ")
        tp = parts[0][0] if parts[0][0] in ["%", "&"] else "b"
        nm = parts[0][1:] if parts[0][0] in ["%", "&"] else parts[0]
        dst = parts[1].split(", ")
        rules[nm] = (tp, dst)
    return rules


L = [s.strip() for s in open("./input.txt").readlines() if s.strip() != ""]
rules = parse_rules(L)
state = {k: {"recent": defaultdict(int), "on": 0} for k in rules}
rule_idx = {k: 0 for k in rules}
for i, r in enumerate(rules):
    rule_idx[r] = i
    for dst in rules[r][1]:
        if dst in rules:
            state[dst]["recent"][r] = 0

for i in range(100000):
    press(i)
hit_ll = {k: np.diff(v) for k, v in hit_ll.items()}

# Check that there's some perfect cycle bullshit because that's how AoC do
assert all([len(set(vals)) == 1 for vals in hit_ll.values()])

print(math.lcm(*[v[0] for v in hit_ll.values()]))
