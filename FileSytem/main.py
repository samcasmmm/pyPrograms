# f = open('demo.txt', 'w')
# str1 = str(input())
# str2 = str(input())
# f.writelines(str1)
# f.writelines(str2)
# f.close()

# f = open('Example.txt', 'r')
# print(f.read(10))
# print(f.readline())
# print(f.readline())
# f.close()

f = open('demo01.txt', 'a')
num = int(input("Enter the Number : "))
for i in range(1, 11):
    f.writelines(f'{num} * {i} = {num*i}\n')
f.close()

