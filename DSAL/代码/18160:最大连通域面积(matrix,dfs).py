size = 0
def dfs(x, y, matrix, neighbors, N, M):
    global size
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if matrix[x][y] == "W":
            size += 1
            matrix[x][y] = "."
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if isvalid(nx, ny, N, M) and matrix[nx][ny] == "W":
                    stack.append((nx, ny))


def isvalid(x, y, N, M):
    return x >= 0 and x < N and y >= 0 and y < M


# Adjust the call to dfs in the solve function
def solve(N, M, matrix):
    global size
    largest_size = 0
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "W":
                dfs(i, j, matrix, neighbors, N, M)
                largest_size = max(largest_size, size)
                size = 0
    return largest_size


T = int(input())
for turn in range(T):
    size = 0
    N, M = map(int, input().split())
    graph = [list(map(str, input())) for _ in range(N)]
    print(solve(N, M, graph))

"""

temp = 0
def search(i,j):
    global temp
    temp += 1
    matrix[i][j] = "."
    for p in dfs:
        if matrix[i+p[0]][j+p[1]] == "W":
            search(i+p[0],j+p[1])


dfs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

T = int(input())
for _ in range(T):
    maxium = 0
    N,M = map(int,input().split())
    matrix = [["."]*(M+2)]
    for i in range(N):
        matrix.append(["."]+list(input())+["."])
    matrix.append(["."]*(M+2))
    #print(matrix)
    for i in range(1,N+1):
        for j in range(1,M+1):
            if matrix[i][j] == "W":
                temp = 0
                search(i,j)
                maxium = max(maxium,temp)
    print(maxium)
"""