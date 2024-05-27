from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m, n = map(int, input().split())
matrix = ([list(map(int, input().split())) for _ in range(m)])
in_queue = [[False for _ in range(n)] for _ in range(m)]


def can_visit(x, y):
    if 0 <= x < m and 0 <= y < n:
        if matrix[x][y] != 2 and not in_queue[x][y]:
            return True
    return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    in_queue[x][y] = True
    step = 0
    while q:
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()
            if matrix[cur_x][cur_y] == 1:
                return step
            for direction in range(4):
                next_x = cur_x + dx[direction]
                next_y = cur_y + dy[direction]
                if can_visit(next_x, next_y):
                    in_queue[next_x][next_y] = True
                    q.append((next_x, next_y))
        step += 1
    return "NO"


step = bfs(0, 0)
print(step)
