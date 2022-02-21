def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()

    greater = []
    lower = []

    for i in a:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quickSort(lower) + [pivot] + quickSort(greater)


numList = [8, 56, 855, 41, 2, 9, 4, 69, 87, 66]
print(quickSort(numList)) # time nlog(n)
