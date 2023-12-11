import numpy as np

L = [s.strip().replace('.', '0').replace('#', '1') for s in open("./input.txt").readlines()]
L = np.array([list(map(int, list(s))) for s in L])

def solve(e_amt):
    r_exp = e_amt * np.cumsum([not np.any(L[i, :]) for i in range(len(L))])
    c_exp = e_amt * np.cumsum([not np.any(L[:, i]) for i in range(len(L[0]))])
    glxs = [(j + c_exp[j], i + r_exp[i]) for i, j in zip(*np.where(L == 1))]
    X = np.diff(sorted([x for x, _y in glxs]))
    Y = np.diff(sorted([y for _x, y in glxs]))
    ret = sum([X[i] * (i + 1) * (len(X) - i) for i in range(len(X))])
    ret += sum([Y[i] * (i + 1) * (len(Y) - i) for i in range(len(Y))])
    return ret

print('part 1:', solve(1))
print('part 2:', solve(999999))
