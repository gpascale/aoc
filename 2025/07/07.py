with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


def part_a():
    splits = 0
    W = len(lines[0])
    L = [0] * W
    L[lines[0].find("S")] = 1
    for i in range(1, len(lines)):
        newL = [0] * W
        for j in range(W):
            if L[j] == 1:
                if lines[i][j] == "^":
                    splits += 1
                    if j > 0:
                        newL[j - 1] = 1
                    if j < W - 1:
                        newL[j + 1] = 1
                else:
                    newL[j] = 1
        L = newL
        s = ["|" if l == 1 else "." for l in L]
        print("".join(s))
    print(splits)


def part_b():
    W = len(lines[0])
    L = [0] * W
    L[lines[0].find("S")] = 1
    for i in range(1, len(lines)):
        newL = [0] * W
        for j in range(W):
            if L[j] > 0:
                if lines[i][j] == "^":
                    if j > 0:
                        newL[j - 1] += L[j]
                    if j < W - 1:
                        newL[j + 1] += L[j]
                else:
                    newL[j] += L[j]
        L = newL
    print(sum(L))


part_a()
part_b()
