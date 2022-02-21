for t in range(int(input())):
    n, a = map(int, input().split())
    if a % 2 != 0:
        if n % 2 == 0:
            print('Even')
        else:
            print('Odd')
    elif n == 1:
        print('Even')
    else:
        print('Impossible')
