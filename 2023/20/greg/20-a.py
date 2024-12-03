from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

rules = {}
state = {}


def add_tuples(a, b):
    return tuple([a[i] + b[i] for i in range(len(a))])


def solve():
    q = []
    for dst in rules["broadcaster"][1]:
        q.append(("broadcaster", dst, 0))

    ret = (1, 0)
    while len(q) > 0:
        from_rule, to_rule, val = q.pop(0)
        ret = add_tuples(ret, (0, 1) if val else (1, 0))
        if not to_rule in rules:
            continue
        typ = rules[to_rule][0]
        if not typ or typ == "%" and val != 0:
            continue

        # update state
        if typ == "%":
            state[to_rule]["on"] = 1 - state[to_rule]["on"]
        elif typ == "&":
            state[to_rule]["recent"][from_rule] = val

        # propagate
        for dst in rules[to_rule][1]:
            if typ == "%":
                q.append((to_rule, dst, state[to_rule]["on"]))
            elif typ == "&":
                n = 0 if all([x == 1 for x in state[to_rule]["recent"].values()]) else 1
                q.append((to_rule, dst, n))
    return ret


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
for r in rules:
    for dst in rules[r][1]:
        if dst in rules:
            state[dst]["recent"][r] = 0

ans = (0, 0)
for c in range(1000):
    ans = add_tuples(ans, solve())
print(ans[0] * ans[1])
