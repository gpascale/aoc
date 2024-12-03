import numpy as np
import json


def cmp(a, b):
    return -1 if a < b else 0 if a == b else 1


def sim(part, rules):
    rulename = "in"
    while True:
        if rulename == "A":
            return 1
        elif rulename == "R":
            return 0
        rule = rules[rulename]
        for r in rule:
            if type(r) == str:
                rulename = r
                break
            if cmp(part[r[0]], r[2]) == r[1]:
                rulename = r[3]
                break


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
                    (
                        s[0],
                        -1 if s[1] == "<" else 1 if s[1] == ">" else 0,
                        int(s[2:].split(":")[0]),
                        s[2:].split(":")[1],
                    )
                )
    return rules


L = [s.strip() for s in open("./input.txt").readlines() if s.strip() != ""]
r = []
parts = []
for l in L:
    r.append(l)
    if l == "BREAK":
        L = L[L.index(l) + 1 :]
        break

for l in L:
    parts.append(
        json.loads(
            l.replace(r"=", ":")
            .replace("x", '"x"')
            .replace("m", '"m"')
            .replace("a", '"a"')
            .replace("s", '"s"')
        )
    )

ret = 0
for part in parts:
    ret += sim(part, parse_rules(r)) * np.sum([v for v in part.values()])
print("part 1:", ret)
