import os
import math
import numpy as np

root = os.path.dirname(os.path.realpath(__file__))

def solve_a(xA, yA, xB, yB, xP, yP):
    memo = {}
    def solve_a_rec(x, y, ans):
        # print(x, y, ans)
        if (x, y) in memo:
            return memo[(x, y)]
        if x == xP and y == yP:
            return ans
        if x > xP:
            memo[(x, y)] = 99999999999
            return memo[(x, y)]
        if y > yP:
            memo[(x, y)] = 99999999999
            return memo[(x, y)]
        ret = min(
            solve_a_rec(x + xA, y + yA, ans + 3),
            solve_a_rec(x + xB, y + yB, ans + 1)
        )
        memo[(x, y)] = ret
        return ret
    r = solve_a_rec(0, 0, 0)
    # print(f'solve({xA}, {yA}, {xB}, {yB}, {xP}, {yP}) = {r}')
    return r
    


def part_a(path):
    with open(path, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    ret = 0
    for i in range(0, len(lines), 4):
        xA, yA = lines[i].replace('Button A: ', '').strip().replace('X+', '').replace('Y+', '').split(', ')
        xB, yB = lines[i+1].replace('Button B: ', '').strip().replace('X+', '').replace('Y+', '').split(', ')
        xP, yP = lines[i+2].replace('Prize: ', '').strip().replace('X=', '').replace('Y=', '').split(', ')
        xA, yA, xB, yB, xP, yP = int(xA), int(yA), int(xB), int(yB), int(xP), int(yP)
        r = solve_a(xA, yA, xB, yB, xP, yP)
        if r < 99999999999:
            ret += r
    return ret

def part_b(path):
    with open(path, "r") as f:
        lines = [s.strip() for s in f.readlines()]
    ret = 0
    for i in range(0, len(lines), 4):
        xA, yA = lines[i].replace('Button A: ', '').strip().replace('X+', '').replace('Y+', '').split(', ')
        xB, yB = lines[i+1].replace('Button B: ', '').strip().replace('X+', '').replace('Y+', '').split(', ')
        xP, yP = lines[i+2].replace('Prize: ', '').strip().replace('X=', '').replace('Y=', '').split(', ')
        xA, yA, xB, yB, xP, yP = int(xA), int(yA), int(xB), int(yB), int(xP), int(yP)
        xP, yP = 10000000000000 + xP, 10000000000000 + yP
        r = np.linalg.solve(np.array([[xA, xB], [yA, yB]]), np.array([xP, yP]))
        r = (int(r[0] + 0.5), int(r[1] + 0.5))
        if r[0] * xA + r[1] * xB == xP and r[0] * yA + r[1] * yB == yP:
            ret += 3 * r[0] + r[1]
    return ret

print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
