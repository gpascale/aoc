def remove(lines):
    num_removed = 0
    new_lines = [l for l in lines]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            num_adj = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (
                        i + k < 0
                        or i + k >= len(lines)
                        or j + l < 0
                        or j + l >= len(lines[i])
                    ):
                        continue
                    if lines[i + k][j + l] == "@":
                        num_adj += 1
            if lines[i][j] == "@" and num_adj < 5:
                new_lines[i] = new_lines[i][:j] + "." + new_lines[i][j + 1 :]
                num_removed += 1
    return new_lines, num_removed


def part_b():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
    orig_count = sum(line.count("@") for line in lines)
    print("\n".join(lines))
    while True:
        new_lines, num_removed = remove(lines)
        if num_removed == 0:
            break
        lines = new_lines
    print("\n")
    print("\n".join(lines))
    new_count = sum(line.count("@") for line in lines)
    print(orig_count - new_count)


part_b()
