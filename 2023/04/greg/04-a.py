import re
import numpy as np


def main():
    lines = [s.strip() for s in open("./04-input.txt").readlines()]
    ret = 0
    for card in lines:
        [winning_nums, my_nums] = re.sub("\d+:", "", card).split("|")
        winners = set([int(x) for x in re.findall(r"\d+", winning_nums)])
        mine = [int(x) for x in re.findall(r"\d+", my_nums)]
        num_winners = len([w for w in mine if w in winners])
        score = (2 ** (num_winners - 1)) if num_winners > 0 else 0
        ret += score
    print(ret)


if __name__ == "__main__":
    main()
