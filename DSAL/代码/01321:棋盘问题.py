def dfs(row, cnt):
    if row == n:
        return 1 if cnt == k else 0
    res = 0
    for i in range(n):
        if broad[row][i] == "#" and columns[i]:
            columns[i] = False
            res += dfs(row + 1, cnt + 1)
            columns[i] = True
    res += dfs(row + 1, cnt)
    return res


while True:
    n, k = map(int, input().split())
    if n == k == -1:
        break
    broad = [list(input()) for i in range(n)]
    columns = [True] * n
    print(dfs(0, 0))