for i in range(int(input())):
    a, b, x = map(int, input().split())
    if 100 <= a <=200 and 100 <= b <= 200 and 1 <= x <= 50:
        ab = b - a
        print(int(ab/x))