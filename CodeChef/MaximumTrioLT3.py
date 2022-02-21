# a = []
# n = int(input())
# for x in range(n):
#     lenNum = input()
#     num = map(int, input())
#     if num == len(lenNum*2):
#         print(num)
#     else:
#         print('Invalid')

# #include<bits/stdc++.h>
# # using namespace std;
# # typedef long long int lli;
# # unordered_map<int,int>m1;
# # void check(){
# #       lli a,b,c,d;
# #       cin>>a>>b>>c>>d;
# #       lli x=a+10*c;
# #       lli y=b+10*d;
# #       if(x==y){cout<<"Draw\n";return;}
# #       cout<<((x>y)?"Chefina":"Chef")<<endl;
# # }
# # int main(){
# #     int t;
# #     cin>>t;
# #     while(t--)
# #     check();
# # }

for _ in range(int(input())):
    n =  int(input())
    x =list(map(int, input().split()))
    x = sorted(x)
    z = (x[-1]-x[0])*x[-2]
    print(z)
