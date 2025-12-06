def part_a(path):
    count = 0
    fresh = []
    lines = [line.strip() for line in open(path, "r").readlines()]
    for line in lines:
        if not line:
            continue
        if "-" in line:
            fresh.append([int(x) for x in line.split("-")])
        else:
            x = int(line)
            for f in fresh:
                if f[0] <= x <= f[1]:
                    count += 1
                    break
    print(count)


def part_b(path):
    count = 0
    f = []
    lines = [line.strip() for line in open(path, "r").readlines()]
    for line in lines:
        if not line:
            break
        if "-" in line:
            f.append([int(x) for x in line.split("-")])

    f = sorted(f, key=lambda x: x[0])

    while True:
        to_remove = None
        for i in range(len(f)):
            for j in range(i + 1, len(f)):
                if f[j][0] <= f[i][1]:
                    to_remove = j
                    if f[j][1] > f[i][1]:
                        # partial overlap
                        f[i][1] = f[j][1]
                    break
            if to_remove:
                break
        if not to_remove:
            break
        f = f[:to_remove] + f[to_remove + 1 :]

    ret = sum([x[1] - x[0] + 1 for x in f])
    print(ret)


part_a("./input.txt")
part_b("./input.txt")
