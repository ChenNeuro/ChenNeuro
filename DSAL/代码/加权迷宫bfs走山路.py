from heapq import heappop, heappush


def bfs(x1, y1):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 移动方向
    q = [(0, x1, y1)]  # 初始化堆
    v = set()  # 走过的路径
    while q:
        t, x, y = heappop(q)  # 省略建堆
        v.add((x, y))
        ### 终止条件 ###
        if x == x2 and y == y2:
            return t
        ### 移动方向 ###
        for dx, dy in dir:  # 这里把（x,y)因为的所有情况走完，因为是算高度差，所以一步走到已经是最优路径。
            nx, ny = x+dx, y+dy
            ### can——visit ###
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#' and (nx, ny) not in v:  # can_visit()模版，if不能则不返回堆
                nt = t + abs(int(matrix[nx][ny])-int(matrix[x][y]))  # 根据题意加上相对高度差
                heappush(q, (nt, nx, ny))  # bfs压入堆（每次处理优先处理当前最优解，但还是贪心）
    return 'NO'


# 主程序
m, n, p = map(int, input().split())
matrix = [list(input().split()) for _ in range(m)]

for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    if matrix[x1][y1] == '#' or matrix[x2][y2] == '#':  # 题目给的补充死亡条件
        print('NO')
        continue
    print(bfs(x1, y1))