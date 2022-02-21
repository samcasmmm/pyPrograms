
for _ in range(int(input())):
    n = int(input())
    l = input()
    a = l.count('1')
    b = l.count('0')
    c = 0
    print(max(c, min(a, b) - 1))
