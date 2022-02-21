n = int(input())
a = list(map(int, input().split()))
c1, c2 = 0, 0
for i in a:
    if i % 2 == 0:
        c1 += 1
    else:
        c2 += 1
if c1 > c2:
    print('READY')
else:
    print('NOT READY')
