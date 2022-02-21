for t in range(int(input())):
    n, d = map(int, input().split())
    a = 1
    b = 1
    if d == 0:
        print(a)
    else:
        for i in range(d):
            if i < 10:
                a = a * 2
            else:
                a = a * 3
            if a > n:
                print(n)
                b = 0
                break
        if b == 1:
            print(a)

# for i in range(int(input())):
#     n, d = map(int, input().split())
# if d <= 10:
#     a = 2 ** d
#     if n > a:
#         print(a)
#     else:
#         print(n)
# elif d >= 11:
#     a = 2 ** d + 1024
#     if n > a:
#         print(a)
#     else:
#         print(n)


# for t in range(int(input())):
#     n, d = map(int, input().split())
#     covid = 0
#     if d <= 10:
#         covid *= 2
#         if n > covid:
#             print(covid)
#         else:
#             print(n)
#     else:
#         covid *= 2
#         if n > covid:
#             print(covid)
#         else:
#             print(n)
