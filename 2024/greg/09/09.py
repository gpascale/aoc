import os

root = os.path.dirname(os.path.realpath(__file__))

def part_a(path):
    with open(path, "r") as f:
        inp = [s.strip() for s in f.readlines()][0]
    layout = []
    for i, c in enumerate(inp):
        c = int(c)
        if i % 2 == 0:
            layout.append((i // 2, c))
        else:
            layout.append((-1, c))
    ret = []
    front, back = 0, len(layout) - 1
    while front < back:
        if layout[front][0] != -1:
            ret.append([layout[front][0]] * layout[front][1])
            front += 1
        elif layout[back][0] == -1:
            back -= 1
        elif layout[back][0] != -1:
            c = min(layout[front][1], layout[back][1])
            ret.append([layout[back][0]] * c)
            layout[front] = (layout[front][0], max(0, layout[front][1] - c))
            layout[back] = (layout[back][0], max(0, layout[back][1] - c))
            if layout[front][1] == 0:
                front += 1
            if layout[back][1] == 0:
                back -= 1
    ret = [c for sublist in ret for c in sublist]
    if front == back and layout[front][0] != -1:
        ret = [*ret, *([layout[front][0]] * layout[front][1])]
    return sum([c * i for i, c in enumerate(ret)])

def part_b(path):
    with open(path, "r") as f:
        inp = [s.strip() for s in f.readlines()][0]
    inp = [int(c) for c in inp]

    gaps, files = [], []
    offset = 0
    for i in range(0, len(inp), 2):
        filelen = int(inp[i])
        gaplen = int(inp[i+1]) if i+1 < len(inp) else 0
        files.append((offset, filelen, int(i // 2)))
        gaps.append((offset + filelen, gaplen))
        offset = offset + filelen + gaplen
    for j in range(len(files) - 1, 0, -1):
        offset, length, fid = files[j]
        for k in range(j):
            if gaps[k][1] >= length:
                files[j] = (gaps[k][0], length, fid)
                gaps[k] = (gaps[k][0] + length, gaps[k][1] - length)
                break

    ret = 0
    for i in range(0, len(files)):
        offset, length, fid = files[i]
        ret += sum([fid * (offset + j) for j in range(length)])
    return ret

print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
