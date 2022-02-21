for i in range(int(input())):
    p, m, v = map(int, input().split())
    if p <= 5 and 6 <= m <= 56 and 1 <= v <= 100:
        if p == 1:
            print(m * v)

        elif p >= 2:
            p -= 1
            a = m - p
            print(a * v)
