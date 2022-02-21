# ATM

def atm(withdraw, balance):
    if withdraw < balance:
        print(balance - withdraw - 0.50)


# withdraw = int(input())
# balance = int(input())
withdraw, balance = map(int,input().strip().split())
atm(withdraw, balance)
