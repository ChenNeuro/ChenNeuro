from collections import deque
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
a = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 5:
            a.append([i,j])
lx = a[1][0] - a[0][0]
ly = a[1][1] - a[0][1]
dire = [[-1,0],[0,1],[1,0],[0,-1]]
v = [[0] * n for i in range(n)]

def bfs(x,y):
    v[x][y] = 1
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        if (mat[x][y] == 9 and mat[x + lx][y + ly] != 1) or (mat[x][y] != 1 and mat[x + lx][y + ly] == 9):
            return 'yes'
        for i in range(4):
            dx = x + dire[i][0]
            dy = y + dire[i][1]
            if 0 <= dx < n and 0 <= dy < n and 0 <= dx + lx < n and 0 <= dy + ly < n and v[dx][dy] == 0 and mat[dx + lx][dy + ly] != 1 and mat[dx][dy] != 1:
                queue.append([dx,dy])
                v[dx][dy] = 1
    return "no"

print(bfs(a[0][0],a[0][1]))