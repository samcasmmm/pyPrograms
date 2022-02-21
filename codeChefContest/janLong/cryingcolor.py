for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    z = [a, b, c]
    if z[0][0] == n and z[1][1] and z[2][2] == n:
        print(0)
        continue
    x = z[0][1] + z[0][2] + z[1][2]
    y = z[1][0] + z[2][0] + z[2][1]
    print(max(x, y))
