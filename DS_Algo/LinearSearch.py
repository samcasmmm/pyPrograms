def LinearSearch(num, key):
    for i in range(len(num)):
        if key == num[i]:
            return f'{key} Found !'
    return f'{key} Not Found !'


numList = [2, 6, 4, 3, 9, 8, 7, 11, 22, 33, 66, 44, 1, 5, 45, 62, 52]
key = 45
print(LinearSearch(numList,key))