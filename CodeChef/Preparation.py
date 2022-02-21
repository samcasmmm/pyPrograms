for _ in range(int(input())):
    m, n, k = map(int, input().split())
    if m == n * k or m < n * k:
        print('ignore =', k * n)
        print('No')
    elif m > n * k:
        print('ignore =', k * n)
        print('Yes')
