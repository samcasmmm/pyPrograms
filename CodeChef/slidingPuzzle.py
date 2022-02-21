def inp():
    tt = input()
    arr = []
    for i in range(0, int(tt)):
        cs = []
        ln = input()
        for i in range(0, int(ln)):
            x = input()
            cs.append(list(map(int, x.split())))
        arr.append(cs)
    run(arr)


def gen_comb_2(N):
    ret = []
    for i in range(0, N - 1):
        for j in range(i + 1, N):
            ret.append([i, j])
    return ret


def chck_pssble(a, b):
    wa = a[2] - a[0]
    ha = a[3] - a[1]
    wb = b[2] - b[0]
    hb = b[3] - b[1]
    if ((wa <= wb) and (ha <= hb)):
        return (0)
    if ((wb <= wa) and (hb <= ha)):
        return (1)
    return None


def calc_score(a, b):
    score = 0
    if (b[3] <= a[3]) and (b[1] >= a[1]):
        pass
    else:
        diff_up = abs(b[3] - a[3])
        diff_low = abs(b[1] - a[1])
        score += min(diff_up, diff_low)
    if (b[2] <= a[2]) and (b[0] >= a[0]):
        pass
    else:
        diff_rt = abs(b[2] - a[2])
        diff_lt = abs(b[0] - a[0])
        score += min(diff_rt, diff_lt)
    return score


def run(arr):
    for cs in arr:
        score = -1
        comb = gen_comb_2(len(cs))
        for i in comb:
            sc = -1
            a = cs[i[0]]
            b = cs[i[1]]
            res = chck_pssble(a, b)
            if res == 0:
                sc = calc_score(b, a)
            if res == 1:
                sc = calc_score(a, b)
            if score == -1:
                score = sc
            elif sc < score:
                score = sc
        print(score)


inp()
