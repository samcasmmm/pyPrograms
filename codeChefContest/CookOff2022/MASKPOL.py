# for _ in range(int(input())):
#     n, a = map(int, input().split())
#     d = n - a
#     if d > a:
#         print(a)
#     elif a > d:
#         print(d)
#     else:
#         print(a)

for _ in range(int(input())):
    n, a = map(int, input().split())
    if n > a and (n - a) > a:
        print(a)
    else:
        print(n - a)
