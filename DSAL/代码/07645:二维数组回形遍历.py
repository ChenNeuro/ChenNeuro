r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
in_queue = [[False for _ in range(c)] for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
result = []


def can_visit(x, y):
    global cnt
    if 0 <= x < r and 0 <= y < c:
        if not in_queue[x][y]:
            cnt += 1
            return True
    return False


def search():
    global cnt, result
    i = 0
    cur_x, cur_y = 0, 0

    while cnt != r*c:
        if can_visit(cur_x, cur_y):
            result.append(matrix[cur_x][cur_y])
            in_queue[cur_x][cur_y] = True
        else:
            cur_x -= dx[i]
            cur_y -= dy[i]
            i += 1
            i %= 4
        cur_x += dx[i]
        cur_y += dy[i]

search()
for i in result:
    print(i)
