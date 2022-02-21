# for t in range(int(input())):
#     s1 = 'abcdefghijklmnopqrstuvwxyz'
#     s2 = []
#     n = int(input())
#     for i in range(n):
#         if i % 3 == 0:
#             s2.append('a')
#         elif i % 3 == 1:
#             s2.append('b')
#         elif i % 3 == 2:
#             s2.append('c')
#         for j in s2:
#             print(j)

for t in range(int(input())):
    k = 0
    s = ''
    n = int(input())
    # a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    #      'j', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    #      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    while n:
        if k == 25:
            k = 0
        s += s1[k]
        k += 1
        n -= 1
    print(s)
