# for i in range(int(input())):
#     n1,n2 = map(int, input().split())
#     if n1 > n2:
#         print('>')
#     elif n1 < n2:
#         print('<')
#     else:
#         print('=')


# muffins3
# for t in range(int(input())):
#     n = int(input())
#     # print(n//2+1)


# valid triangle
# for t in range(int(input())):
#     a, b, c = map(int, input().split())
#     if a + b + c == 180:
#         print('YES')
#     else:
#         print('NO')


# for t in range(int(input())):
#     a, b = map(int, input().split())
#     print(a, a+b)


# ceilrcpt
# t = int(input().strip())
# for i in range(t):
#     a = int(input().strip())
#     m = 0
#     for j in range(11, -1, -1):
#         b = 2 ** j
#         while a >= b:
#             a = a - b
#             m += 1
#     print(m)

T = int(input().strip())

for i in range(T):
    p = int(input().strip())
    menuitems = 0
    for i in range(11, -1, -1):
        M = 2 ** i
        while p >= M:
            p = p - M
            menuitems += 1
    print(menuitems)
