from collections import defaultdict

right_turn = set(["RD", "DL", "LU", "UR"])
move = {"D": [0, 1], "U": [0, -1], "R": [1, 0], "L": [-1, 0]}
inside = {"D": [-1, 0], "U": [1, 0], "R": [0, 1], "L": [0, -1]}

dec = "0123456789abcdef"


def solve(S):
    bounds = [[999999999, -999999999], [999999999, -999999999]]
    starts = []
    ends = []

    x = 0
    y = 0
    for _, _, color in S:
        num_steps, di = [int(color[:5], 16), "RDLU"[int(color[5], 16)]]
        # print(di, num_steps)
        x += move[di][0] * num_steps
        y += move[di][1] * num_steps
        bounds[0][0] = min(bounds[0][0], x)
        bounds[0][1] = max(bounds[0][1], x)
        bounds[1][0] = min(bounds[1][0], y)
        bounds[1][1] = max(bounds[1][1], y)

    x = -bounds[0][0]
    y = -bounds[1][0]
    W = bounds[0][1] - bounds[0][0] + 1

    starts = [[] for _ in range(W)]
    ends = [[] for _ in range(W)]

    turns = []
    for i in range(len(L)):
        di = "RDLU"[int(S[i][2][5], 16)]
        di_next = "RDLU"[int(S[(i + 1) % len(S)][2][5], 16)]
        turns.append(str(f"{di}{di_next}"))
    num_left_turns = len([turn for turn in turns if turn not in right_turn])

    sums = defaultdict(int)
    for i, step in enumerate(S):
        _, _, color = step
        num_steps, di = [int(color[:5], 16), "RDLU"[int(color[5], 16)]]
        sums[di] += num_steps
        if di == "R":
            starts[y].append((x))
            ends[y].append((x + num_steps))
            x += num_steps
        elif di == "L":
            starts[y].append((x - num_steps))
            ends[y].append((x))
            x -= num_steps
        elif di == "U":
            for yy in range(y, y - num_steps - 1, -1):
                starts[yy].append((x))
            y -= num_steps
        elif di == "D":
            for yy in range(y, y + num_steps + 1, 1):
                ends[yy].append((x))
            y += num_steps

    starts = [sorted(list(set(s))) for s in starts]
    ends = [sorted(list(set(s))) for s in ends]
    ret = 0
    for i in range(len(starts)):
        for j in range(len(starts[i])):
            ret += ends[i][j] - starts[i][j] + 1
    ret -= num_left_turns
    return ret


L = [s.strip() for s in open("./input.txt").readlines() if s]
steps = [s.replace("(", "").replace(")", "").replace("#", "").split(" ") for s in L]

print("part 2:", solve(steps))
