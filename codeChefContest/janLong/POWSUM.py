# def power(p):
#     p = p - 1
#     while (p & p - 1) != 0:
#         p = p & p - 1
#         return p << 1
#
#
# for t in range(int(input())):
#     a = int(input())
#     x = []
#     y = []
#     i, j = 0, 0
#     mini, k, c, s, ans, m = 0, 0, 1, 0, 0, 0
#     for j in range(a):
#         x[i] = int(input())
#         y[i] = x[i]
#         s = s+ x[i]
#     y.sort()
#     m = power(s)
#     mini = y[0]
#     s = s - mini
#     ans = s
#     c = (m-s)/mini
#     if c == 1:
#         print('0')
#     else:
#         print('1')
#     print('1'+c)

