for i in range(int(input())):
    a = int(input())
    if a > 1:
        for j in range(2, int(a / 2) + 1):
            if (a % j) == 0:
                print('No')
                break
        else:
            print('Yes')
    else:
        print('No')
