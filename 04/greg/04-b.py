import re

num_winners = []
scores = []
N = 0


def score_card(i):
    global num_winners, scores, N
    if scores[i] != -1:
        return scores[i]
    scores[i] = 1
    for j in range(i + 1, min(i + num_winners[i] + 1, len(scores))):
        scores[i] += score_card(j)
    return scores[i]


def solve_part_2(cards):
    global num_winners, scores, N
    N = len(cards)
    num_winners = [0 for _ in range(N)]
    scores = [-1 for _ in range(N)]
    for i, card in enumerate(cards):
        [winning_nums, my_nums] = re.sub("\d+:", "", card).split("|")
        winners = set([int(x) for x in re.findall(r"\d+", winning_nums)])
        mine = [int(x) for x in re.findall(r"\d+", my_nums)]
        num_winners[i] = len([w for w in mine if w in winners])
    return sum([score_card(i) for i in range(N)])


def main():
    lines = [s.strip() for s in open("./04-input.txt").readlines()]
    result = solve_part_2(lines)
    print(result)


if __name__ == "__main__":
    main()
