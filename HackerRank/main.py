# tup = (1,22,3)
# print(hash(tup))


def mutate_string(string, position, character):
    a = string[:position] + character + string[position+1:]
    return a


string = str(input())
position, char = map(str, input().split())
position = int(position)

a = mutate_string(string, position, char)
print(a)
from typing import List

a = map(int, input().split())
target = int(input())
alist = list(a)
dict = {}
for i,v in enumerate(a):
    ans = target - alist[i]
    if ans in dict:
        print(i, dict[ans])
    dict[v] = i
print(dict)


a = [5, 6, 3, 7, 9, 4, 1]
target = 12
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if a[i] + a[j] + a[k] == target:
                print(i+j+k==target)
