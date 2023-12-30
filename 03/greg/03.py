import re
import numpy as np


def solve_part_1(grid):
    W = len(grid[0])
    H = len(grid)
    ret = 0
    for row in range(H):
        num_matches = [m for m in re.finditer(r"(\d+)", grid[row])]
        for match in num_matches:
            (num, start, end) = (match[0], match.span()[0], match.span()[1])
            is_part_num = False
            for i in range(max(row - 1, 0), min(row + 2, H)):
                for j in range(max(start - 1, 0), min(end + 1, W)):
                    if grid[i][j] in "!@#$%.&*()/+-=~,<>?":
                        is_part_num = True
            if is_part_num:
                ret += int(num)
    return ret


def solve_part_2(grid):
    W = len(grid[0])
    H = len(grid)
    ret = 0

    nums = [[] for _i in range(H)]
    for row in range(H):
        nums[row] = [
            (int(m[0]), m.span()[0], m.span()[1] - 1)
            for m in re.finditer(r"(\d+)", grid[row])
        ]

    for row in range(H):
        for col in range(W):
            if grid[row][col] not in "!@#$%.&*()/+-=~,<>?":
                continue
            gears = []
            for r in range(max(row - 1, 0), min(row + 2, H)):
                for match in nums[r]:
                    if match[1] <= col + 1 and match[2] >= col - 1:
                        gears.append(int(match[0]))
            if len(gears) >= 2:
                ret += np.prod(gears)

    return ret


def main():
    lines = [s.strip() for s in open("./03-input.txt").readlines()]

    print("part 1:", solve_part_1(lines))
    print("part 2:", solve_part_2(lines))


if __name__ == "__main__":
    main()
