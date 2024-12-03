import numpy as np
import re
import os

root = os.path.dirname(os.path.realpath(__file__))


def part_a(path):
    with open(path, "r") as f:
        s = f.read()
    muls = re.findall("mul\(\d{1,3},\d{1,3}\)", s)
    ret = 0
    for m in muls:
        a, b = m[4:-1].split(",")
        ret += int(a) * int(b)
    return ret


def part_b(path):
    with open(path, "r") as f:
        s = f.read()
    instrs = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", s)
    ret = 0
    is_do = 1
    for instr in instrs:
        if instr == "do()":
            is_do = 1
        elif instr == "don't()":
            is_do = 0
        elif is_do:
            a, b = instr[4:-1].split(",")
            ret += int(a) * int(b)
    return ret


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example-a.txt"))
print("Part B:", part_b(f"{root}/input-example-b.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
