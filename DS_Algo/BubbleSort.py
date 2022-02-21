def bSort(a):
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


l = [3, 2, 1, 5, 6, 8, 7]
l1 = [4, 6, 6, 9, 41, 2, 8, 4, 96, 8, 5, 6, 4, 9, 5, 6]
print(bSort(l1))
