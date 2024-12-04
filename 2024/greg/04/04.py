import numpy as np
import re
import os

root = os.path.dirname(os.path.realpath(__file__))


def diags(s):
    return [np.diagonal(s, i) for i in range(-s.shape[0] + 1, s.shape[1])]


def part_a(path):
    with open(path, "r") as f:
        s = np.array([list(s.strip()) for s in f.readlines()])
    mega_word = []
    for i in range(0, 4):
        mega_word.append(list(np.rot90(s, i)))
        mega_word.append(diags(np.rot90(s, i)))
    mega_word = [x for xs in mega_word for x in xs]  # flatten
    mega_word = " ".join(["".join(w) for w in mega_word])
    return len(re.findall("XMAS", mega_word))


def part_b(path):
    with open(path, "r") as f:
        s = np.array([list(s.strip()) for s in f.readlines()])
    ret = 0
    for i in range(1, s.shape[0] - 1):
        for j in range(1, s.shape[1] - 1):
            if s[i, j] == "A":
                c = "".join(
                    [s[i + y, j + x] for x, y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
                )
                if (
                    c.count("S") == 2
                    and c.count("M") == 2
                    and s[i - 1, j - 1] != s[i + 1, j + 1]
                ):
                    ret += 1
    return ret


print("Example Input:")
print("Part A:", part_a(f"{root}/input-example.txt"))
print("Part B:", part_b(f"{root}/input-example.txt"))

print("\nReal Input:")
print("Part A:", part_a(f"{root}/input.txt"))
print("Part B:", part_b(f"{root}/input.txt"))
