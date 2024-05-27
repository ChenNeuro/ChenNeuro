import copy

m, n, p = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))


def add(lst):
    for i in range(len(lst) - 1):
        if lst[i] != 0:
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    lst[i], lst[j] = 0, 2 * lst[i]
                    break
                elif lst[j] == 0:
                    pass
                else:
                    break
    ans = []
    count = 0
    for i in lst:
        if i != 0:
            ans.append(i)
            count += 1
    return [0] * (len(lst) - count) + ans


def move(matrix, dirc):
    new = copy.deepcopy(matrix)
    if dirc == "right":
        for i in range(m):
            newrow = add(new[i])
            new[i] = newrow
    elif dirc == "down":
        for j in range(n):
            temp = [new[i][j] for i in range(m)]
            newline = add(temp)
            for k in range(m):
                new[k][j] = newline[k]
    elif dirc == "left":
        for i in range(m):
            temp = [new[i][j] for j in range(n - 1, -1, -1)]
            newrow = add(temp)
            for k in range(n):
                new[i][n - 1 - k] = newrow[k]
    else:
        for j in range(n):
            temp = [new[i][j] for i in range(m - 1, -1, -1)]
            newline = add(temp)
            for k in range(m):
                new[m - 1 - k][j] = newline[k]
    return new


result = 0


def calculate(matrix, num):
    global result
    if num == p:
        result = max(result, max(max(matrix[i]) for i in range(m)))
        return
    calculate(move(matrix, "up"), num + 1)
    calculate(move(matrix, "down"), num + 1)
    calculate(move(matrix, "left"), num + 1)
    calculate(move(matrix, "right"), num + 1)


calculate(matrix, 0)
print(result)