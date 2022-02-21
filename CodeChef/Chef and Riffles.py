# for t in range(int(input())):
#     n, k = map(int, input().split())
#     arr = []
#     zrr = []
#     answer, ans = [], []
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             arr.append(i)
#         if i % 2 != 0:
#             zrr.append(i)
#     zrr.extend(arr)
#
#     if k > 1:
#         for j in range(k):
#             ans = zrr[::2]
#             for kans in ans:
#             answer = zrr[::1]
#         print('1', ans)
#         print('2', answer)
#     else:
#         print(zrr)

    # if k == 1:
    #     print(zrr)
    # else:
    #     for ij in range(1, k):
    #         for count, j in enumerate(zrr):
    #             if count % 2 == 1:
    #                 odd.append(j)
    #             else:
    #                 even.append(j)
    #         ans = odd + even
    #     print(ans)
