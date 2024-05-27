import statistics
n = int(input())
pos = [sum(map(int, i[1:-1].split(","))) for i in input().split()]
# print(pos)  # [(100, 200), (50, 50), (100, 300), (150, 50), (50, 50)]
prices = [int(i) for i in input().split()]
# print(prices)  [100, 300, 200, 400, 500]
p2v = statistics.median([pos[i]/prices[i] for i in range(n)])
mid_price = statistics.median(prices)
ans = 0
for i in range(n):
    if prices[i] < mid_price and (pos[i]/prices[i]) > p2v:
        ans += 1
print(ans)