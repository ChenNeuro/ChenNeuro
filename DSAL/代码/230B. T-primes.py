import math
n = int(1e6)
ans = [False]*(n+1)
ans[1] = True
ans_list = set()
for i in range(2,int(math.sqrt(n+1)+1)):
    if not ans[i]:
        for j in range(i**2,n+1,i):
            ans[j]= True
for i in range(2,n+1):
    if not ans[i]:
        ans_list.add(i)
print(ans_list)

n = int(input())
nlist = list(map(int,input().split()))
for i in nlist:
    if math.pow(i,0.5) == int(math.pow(i,0.5)) and int(math.pow(i,0.5)) in ans_list:
        print("YES")
    else:
        print("NO")