# for i in range(int(input())):
#     l = []
#     a, b, c = map(int, input().strip().split())
#     l.append(a)
#     l.append(b)
#     l.append(c)
#     l.sort()
#     print(l[-2])


#betterway
for i in range(int(input())):
    t = list(map(int,input().split()))
    t.sort()
    print(t[-2])