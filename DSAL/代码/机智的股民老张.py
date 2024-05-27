line = list(map(int, input().split()))
low = float('inf')
ans = 0
for i in range(len(line)):
    low = min(low,line[i])
    ans = max(ans,line[i]-low)
print(ans)