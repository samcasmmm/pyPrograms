# fact = 1
# n = 5
# while n > 1:
#     fact *= n
#     n -= 1
# print(fact)


for _ in range(int(input())):
    fact = 1
    n = int(input())
    while n > 1:
        fact *= n
        n -= 1
    print(fact)
