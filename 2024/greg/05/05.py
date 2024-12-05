import os
from collections import defaultdict

root = os.path.dirname(os.path.realpath(__file__))


def part_a(path):
    with open(path, "r") as f:
        lines = f.readlines()
    rules, updates = lines[: lines.index("\n")], lines[lines.index("\n") + 1 :]
    rules = [[int(x) for x in rule.split("|")] for rule in rules]
    rules = set([tuple(r) for r in rules])
    updates = [[int(x) for x in update.split(",")] for update in updates]

    ret = 0

    for update in updates:
        is_good = 1
        for i in range(len(update) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if (update[i], update[j]) in rules:
                    is_good = 0
                    break
            if not is_good:
                break
        if is_good:
            ret += update[len(update) // 2]
    return ret


def part_b(path):
    with open(path, "r") as f:
        lines = f.readlines()
    rules, updates = lines[: lines.index("\n")], lines[lines.index("\n") + 1 :]
    rules = [[int(x) for x in rule.split("|")] for rule in rules]
    rules = set([tuple(r) for r in rules])
    updates = [[int(x) for x in update.split(",")] for update in updates]

    ret = 0

    for update in updates:
        updated_once = False
        # repeatedly fix bad pairs by moving Y to just before X until no bad pairs left
        while True:
            fixed_one = False
            for i in range(len(update) - 1, 0, -1):
                for j in range(i - 1, -1, -1):
                    if (update[i], update[j]) in rules:
                        update = (
                            update[:j] + [update[i]] + update[j:i] + update[i + 1 :]
                        )
                        fixed_one = True
                        updated_once = True
            if not fixed_one:
                if updated_once:
                    ret += update[len(update) // 2]
                break
    return ret


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
