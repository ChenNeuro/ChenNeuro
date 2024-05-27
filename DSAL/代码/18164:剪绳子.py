import heapq
n = int(input())
nums = list(map(int, input().split()))
heapq.heapify(nums)
res = 0

while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    res += a+b
    heapq.heappush(nums, a+b)
print(res)