import heapq
ans = []


def bfs(x, y):
    d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    queue = []
    heapq.heappush(queue, [0, x, y])
    check = set()
    check.add((x, y))
    while queue:
        step, x, y = map(int, heapq.heappop(queue))
        if martix[x][y] == 1:
            ans.append(step)
        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if martix[dx][dy] != 2 and (dx, dy) not in check:
                if martix[dx][dy] == 3:
                    heapq.heappush(queue, [step + 0, dx, dy])
                else:
                    heapq.heappush(queue, [step + 1, dx, dy])
                check.add((dx, dy))
    if ans:
        return min(ans)
    return "NO"


m, n = map(int, input().split())
martix = [[2] * (n + 2)] + [[2] + list(map(int, input().split())) + [2] for i in range(m)] + [[2] * (n + 2)]
print(bfs(1,1))