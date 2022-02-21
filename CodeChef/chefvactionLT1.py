# t,a,b,c = map(int,input().split())
t = int(input())
while t > 0:
    a, b, c = map(int, input().split(' '))
    if a + b > c:
        print('TRAIN')
    elif a + b == c:
        print('EQUAL')
    else:
        print('PLANEBUS')
    t -= 1
