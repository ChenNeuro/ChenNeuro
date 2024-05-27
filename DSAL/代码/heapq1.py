import heapq
N = int(input())
A = list(map(int, input().split()))
heapq.heapify(A)
price = 0
while len(A) != 1:
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    heapq.heappush(A, a+b)
    price += a+b
print(price)