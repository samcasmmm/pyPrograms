for t in range(int(input())):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    a3, b3 = map(int, input().split())
    print(max(a1+b1, a2+b2, a3+b3))


    # c1 = a1 + b1
    # c2 = a2 + b2
    # c3 = a3 + b3
    # print(max(c1, c2, c3))
