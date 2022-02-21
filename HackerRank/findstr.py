def countstr(a, b):
    for i in range(len(a)):
        c = a.count(b)
        return c

a = input()
b = input()
print(countstr(a, b))
