# a = 10
# b = 9
# c = 9
#
# print(id(a))
# print(id(b))
# print(id(c))

# a1 = 41+1j
# print(type(a1))
#
# a = 8
#
# b = float(a)
# print(type(b))

# print(a != b)

# x = True
# print(not x)

# Dec2Bin

# num = int(input("Enter the Number : "))
# binum = [0] * num
# i = 0
# while num > 0:
#     binum[i] = num % 2
#     num = int(num / 2)
#     i += 1
# for j in range(i - 1, -1, -1):
#     print(binum[j], end='')


# age = int(input())
# if 10 < age < 85:
#     if age > 18:
#         print("You can drive")
#     elif age == 18:
#         print("we can't decide that !! Give Test first")
#     else:
#         print("You can't drive")
# else:
#     print("We can't accept req from below 10year and above 85year")

# d = {'python': 'easy',
#      'c++': 'hard',
#      'c': 'intermediate',
#      'js': 'medium'}
# print(d.keys())
# a = str(input("Enter a Name : "))
# if a in d:
#     print(d[a])
# else:
#     print("Not in Dict")

# pattern 1

# num = int(input('Number : '))
# boolean = int(input('0 or 1 : '))
#
# if boolean == 1:
#     for i in range(0, num):
#         for j in range(0, i+1):
#             print("* ", end="")
#         print('\r')
# elif boolean == 0:
#     for i in range(num, 0, -1):
#         for j in range(0, i):
#             print("* ", end="")
#         print('\r')

# f = open('Example.txt', 'r')
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()