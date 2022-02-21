for t in range(int(input())):
    n, x = map(int, input().split())
    numList = list(map(int, input().split()))
    c = 0
    z = 0
    numList.sort()
    numList.reverse()
    if sum(numList) < x:
        print(-1)
    elif sum(numList) == x:
        print(n)
    else:
        for i in numList:
            if z < x:
                z += i
                c += 1
            else:
                break
        print(c)
