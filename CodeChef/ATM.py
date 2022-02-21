# x, y = map(float, input().strip().split())
#
# if x < y - 0.50 and x % 5 == 0:
#     print(y - x - 0.50)
# else:
#     print(x)

x,y = map(float, input().split())

if x <= y-0.5 and x % 5==0:
    print("%.2f"%(y-x-0.50))
else:
    print("%.2f"%y)