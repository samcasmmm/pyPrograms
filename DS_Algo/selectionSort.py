def selSort(n):
    for i in range(len(n)):
        cur_index = i
        for j in range(i, len(n)):
            if n[cur_index] > n[j]:
                cur_index = j
        n[i], n[cur_index] = n[cur_index], n[i]
    return n


num = [3, 2, 1, 5, 4, 6, 9, 8, 7]
print(selSort(num))

