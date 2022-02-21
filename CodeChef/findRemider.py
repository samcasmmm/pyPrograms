times = int(input())
for i in range(times):
    num, div = map(int, input().split())
    print(num % div)