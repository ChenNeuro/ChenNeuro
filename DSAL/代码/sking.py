R, C = map(int, input().split())
v = [False for i in range(C)]*R


def can_visited(nx,ny):
    if 0 <= nx < R and 0 <= ny < C and area[nx][ny] != '#' and (nx, ny) not in v:
        return True


area = []
for _ in range(R):
    area.append(list(map(int,input().split())))
maxium = 0

way = [[-1,0],[1,0],[0,-1],[0,1]]
cnt = 0


def search(x1,y1):
    v = set()
    v.add(x1,y1)
    for direction in way:
        nx = x1 + direction[0]
        ny = y1 + direction[1]
        if can_visited(nx,ny) and area[x1][y1] > area[nx][ny]:
            search(nx,ny)
            v.remove(x1,y1)

    if area



for i in range(1, R + 2):
    for j in range(1, C + 2):
        search(i,j)
print(maxium)


