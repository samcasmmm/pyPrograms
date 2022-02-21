
for t in range(int(input())):
    s = input()
    n = len(s)
    if n == 1:
        print('No')
        continue
    a = 0
    b = -1
    i = 0
    while i < n:
        if s[i] == '1':
            a += 1
            b = i + 1
        i += 1
    if a == 0 or (a == 1 and b == n):
        print('No')
    else:
        print('Yes')



# try 1

# def binaryToDecimal(binary):
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while binary != 0:
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary // 10
#         i += 1
#     return decimal
#
#
# def isPrime(n):
#     if n % 2 == 0:
#         print('No')
#     else:
#         print('Yes')
#
# for t in range(int(input())):
#     num = int(input())
#     a = binaryToDecimal(num)
#     isPrime(a)

# try 2


# for t in range(int(input())):
#     flag = None
#     s = str(input())
#     for i in range(len(s)):
#         if s[i] == '1' and s[i + 1] == '1' or s[i + 1] == '0':
#             flag = True
#             print('Yes')
#             break
#     if flag == False:
#         print('No')
