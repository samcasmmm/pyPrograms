for i in range(int(input())):
    xa, xb, Xa, Xb = map(int, input().split())
    if 100 <= xa <= 200 and 400 <= xb <= 500 and 1000 <= Xa <= 1200 and 1000 <= Xb <= 1500:
        a = Xa / xa
        b = Xb / xb
        print(int(a+b))