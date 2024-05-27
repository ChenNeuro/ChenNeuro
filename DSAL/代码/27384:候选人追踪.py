import heapq
n,k = map(int,input().split())
lst = list(map(int, input().split()))
arr = sorted([lst[2*i],lst[2*i+1]] for i in range(n))
vote = [0 for i in range(314160)]
s = list(map(int, input().split()))
mark_dict = {}
for i in range(k):
    mark_dict[s[i]] = 0
if k == 314159:
    print(arr[-1][0])
    exit()
most,least = 0,0
ans = 0
for j in range(n):
    v = arr[j][1]
    if v in mark_dict:
        mark_dict[v] += 1
        if mark_dict[v]-1 <= least or least == 0:
            temp = list(mark_dict.values())
            heapq.heapify(temp)
            least = temp[0]
    else:
        vote[v] += 1
        most = max(most,vote[v])
    if j < n-1 and arr[j+1][0] != arr[j][0] and least > most:
        ans += arr[j+1][0]-arr[j][0]
print(ans)
