import heapq
n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
ans = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    ans += a + b
    heapq.heappush(arr, a+b)
print(ans)
