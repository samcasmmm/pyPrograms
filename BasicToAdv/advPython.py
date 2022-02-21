# try

# while True:
#     print("Press q to quit")
#     a = input("enter a number")
#     a = int(a)
#
#     if a == 'q':
#         break
#     if a > 6:
#
#         print("Greater than 6")

## Readline try except
# def readFile(file):
#     try:
#         with open(file, 'r') as f:
#             print(f.read())
#     except FileNotFoundError as e:
#         print(file, e)
#
#
# readFile('1.txt')
# readFile('2.txt')
# readFile('3.txt')

# table list comprehension

# num = int(input("Number : "))
# a = [num * i for i in range(1, 11)]
# print(a)
#
# with open('table.txt', 'a') as f:
#     f.writelines(f'table of {num} = {str(a)} \n ')

