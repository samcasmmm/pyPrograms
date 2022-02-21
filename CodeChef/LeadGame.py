# for i in range(int(input())):
#     lead = []
#     p = list(map(int, input().split()))
#     x = max(p) - min(p)
#     lead.append(x)
#     print(max(lead))


# for i in range(int(input())):
#     w = None
#     l = 0
#     p1, p2 = map(int, input().split())
#     if p1 > p2:
#         diff = p1 - p2
#         if diff > l:
#             lead = diff
#             w = 1
#     else:
#         diff = p2 - p1
#         if diff > l:
#             l = diff
#             w = 2
#     print(w, l)

# l = []
# w = 0
# for i in range(int(input())):
#     p1, p2 = map(int, input().split())
#     if p1 > p2:
#         diff = p1 - p2
#         l.append(p1-p2)
#         if diff > max(l)
#             w = 1
#     else:
#         l.append(p2 - p1)
#         w = 2
# print(w, max(l))