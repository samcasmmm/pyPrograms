for _ in range(int(input())):
    a, b = map(int, input().split())
    x = input()
    z = x
    while b > 0:
        c = (z[:b])[::-1] + z[b:]
        b -= 1
        z = c
    print(z)
