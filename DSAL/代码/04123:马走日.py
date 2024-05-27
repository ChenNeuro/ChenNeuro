T = int(input())
dir = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y, n, m, visited, count):
    if count == n * m:  # 看是否自我湮灭
        return 1
    total = 0
    visited[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy  # 举棋子
        if valid(nx, ny, n, m) and not visited[nx][ny]:
            total += dfs(nx, ny, n, m, visited, count + 1)  # 放棋子
    visited[x][y] = False  # 回溯
    return total


for _ in range(T):
    n, m, x, y = map(int, input().split())
    visited = [[False]*m for _ in range(n)]
    print(dfs(x, y, n, m, visited, 1))
