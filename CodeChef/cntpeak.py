for t in range(int(input())):
    n = int(input())
    if n < 3:
        print(0)
    else:
        print(10 * (n - 2) * (3 ** (n - 3)))
