for i in range(int(input())):
    t1, t2, r1, r2 = map(int, input().split())
    a = (t1**2) / (r1**3)
    b = (t2**2) / (r2**3)
    if a == b:
        print('Yes')
    else:
        print('No')
