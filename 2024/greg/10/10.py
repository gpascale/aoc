import os

root = os.path.dirname(os.path.realpath(__file__))

def solve_a(r, c, grid, memo):
    if memo[r][c] is not None:
        return memo[r][c]
    if grid[r][c] == '9':
        return set([(r, c)])
    ret = set()
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and int(grid[nr][nc]) - int(grid[r][c]) == 1:
            ret = ret | solve_a(nr, nc, grid, memo)
    memo[r][c] = ret
    return ret

def part_a(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    memo = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    ret = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '0':
                peaks = solve_a(r, c, grid, memo)
                score = len(peaks)
                ret += score
    return ret


def solve_b(r, c, grid, memo):
    if memo[r][c] is not None:
        return memo[r][c]
    if grid[r][c] == '9':
        return 1
    ret = 0
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and int(grid[nr][nc]) - int(grid[r][c]) == 1:
            ret = ret + solve_b(nr, nc, grid, memo)
    memo[r][c] = ret
    return ret

def part_b(path):
    with open(path, "r") as f:
        grid = [s.strip() for s in f.readlines()]
    memo = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    ret = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '0':
                score = solve_b(r, c, grid, memo)
                # print(r, c, score)
                ret += score
    return ret

print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
