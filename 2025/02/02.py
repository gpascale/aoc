from math import floor, log10

with open("input.txt", "r") as f:
    lines = f.readlines()
    ranges = [[int(x) for x in r.split("-")] for r in lines[0].strip().split(",")]


def part_a():
    ret = 0
    for r in ranges:
        for x in range(r[0], r[1] + 1):
            num_digs = floor(log10(x)) + 1
            if num_digs % 2 != 0:
                continue
            a = x % (10 ** (num_digs // 2))
            b = x // (10 ** (num_digs // 2))
            if a == b:
                ret += x
    print(ret)


def part_b():
    ret = 0
    for r in ranges:
        for x in range(r[0], r[1] + 1):
            num_digs = floor(log10(x)) + 1
            for d in range(1, num_digs // 2 + 1):
                if num_digs % d != 0:
                    continue
                nums = [x // (10**c) % (10**d) for c in range(0, num_digs, d)]
                if all(nums[i] == nums[0] for i in range(1, len(nums))):
                    ret += x
                    break
    print(ret)


part_a()
part_b()
