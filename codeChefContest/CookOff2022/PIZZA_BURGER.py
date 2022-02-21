for t in range(int(input())):
    x, y, z = map(int, input().split())
    if y <= x:
        print('Pizza')
    elif z <= x:
        print('Burger')
    else:
        print('Nothing')
