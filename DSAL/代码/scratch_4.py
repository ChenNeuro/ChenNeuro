# 欧拉筛
import math
n = int(1e5)
ans = [False]*(n+1)
ans[1] = True
ans_list = []
for i in range(2,int(math.sqrt(n+1)+1)):
  if not ans[i]:
    for j in range(i**2,n+1,i):
      ans[j]= True
for i in range(2,n+1):
  if not ans[i]:
    ans_list.append(i)
print(ans_list)