# 23 工学院 苏王捷
import heapq


def bfs(x, y):
    d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    queue = []
    heapq.heappush(queue, [0, x, y])
    check = set()
    check.add((x, y))
    while queue:
        step, x, y = map(int, heapq.heappop(queue))
        if matrix[x][y] == 1:
            return step
        for i in range(4):
            dx, dy = x + d[i][0], y + d[i][1]
            if matrix[dx][dy] != 2 and (dx, dy) not in check:
                heapq.heappush(queue, [step + 1, dx, dy])
                check.add((dx, dy))
    return "NO"


m, n, turn = map(int, input().split())
matrix = [[2] * (n + 2)] + [[2] + list(map(int, input().split())) + [2] for i in range(m)] + [[2] * (n + 2)]
for _ in range(turn):
    a,b = map(int, input().split())
    print(bfs(b,a) if matrix[b][a] != 2 else "NO")

