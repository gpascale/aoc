import os
from math import floor, log

root = os.path.dirname(os.path.realpath(__file__))


def solve_a(cur, nums, target):
    if not len(nums):
        # print(target, cur)
        return target if cur == target else 0
    if cur > target:
        return 0
    next_num = nums[0]
    return solve_a(cur + next_num, nums[1:], target) or solve_a(
        cur * next_num, nums[1:], target
    )


def part_a(path):
    with open(path, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    ret = 0
    for line in lines:
        target = int(line[: line.index(":")])
        nums = [int(x) for x in line[line.index(":") + 1 :].strip().split()]
        ret += solve_a(nums[0], nums[1:], target)
    return ret


def solve_b(cur, nums, target):
    if not len(nums):
        return target if cur == target else 0
    if cur > target:
        return 0
    next_num = nums[0]
    return (
        solve_b(cur + next_num, nums[1:], target)
        or solve_b(cur * next_num, nums[1:], target)
        or solve_b(cur * (10 ** (floor(log(next_num, 10)) + 1)) + next_num, nums[1:], target)
    )


def part_b(path):
    with open(path, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    ret = 0
    for line in lines:
        target = int(line[: line.index(":")])
        nums = [int(x) for x in line[line.index(":") + 1 :].strip().split()]
        ret += solve_b(nums[0], nums[1:], target)
    return ret


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
