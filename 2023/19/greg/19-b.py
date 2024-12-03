import numpy as np


def solve(rules):
    q = [({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}, "in", 0)]
    ans = []
    while len(q):
        cur, rulename, idx = q.pop(0)
        r = rules[rulename][idx] if rulename in rules else rulename

        # handle terminal rules
        if type(r) == str:
            if r == "A":
                ans.append(cur)
            elif r != "R":
                q.append((cur, r, 0))
            continue

        # handle normal rules - branch search
        if r[1] == "<":
            cur_in = {**cur, r[0]: (cur[r[0]][0], r[2] - 1)}
            cur_out = {**cur, r[0]: (r[2], cur[r[0]][1])}
        else:
            cur_in = {**cur, r[0]: (r[2] + 1, cur[r[0]][1])}
            cur_out = {**cur, r[0]: (cur[r[0]][0], r[2])}
        if cur_in[r[0]][0] <= cur_in[r[0]][1]:
            q.append((cur_in, r[3], 0))
        if cur_out[r[0]][0] <= cur_out[r[0]][1]:
            q.append((cur_out, rulename, idx + 1))
    ret = 0
    for a in ans:
        ret += np.prod([max(a[c][1] - a[c][0] + 1, 0) for c in ["x", "m", "a", "s"]])
    return ret


def parse_rules(R):
    rules = {}
    for s in R:
        name = s.split("{")[0]
        r = s[len(name) :].replace("{", "").replace("}", "").split(",")
        rules[name] = []
        for s in r:
            if ":" not in s:
                rules[name].append(s)
            else:
                rules[name].append(
                    (s[0], s[1], int(s[2:].split(":")[0]), s[2:].split(":")[1])
                )
    return rules


# L = [s.strip() for s in example.split("\n") if s.strip() != ""]
L = [s.strip() for s in open("./input.txt").readlines() if s.strip() != ""]
r = [l for l in L[: L.index("BREAK")]]
print("part 2:", solve(parse_rules(r)))
