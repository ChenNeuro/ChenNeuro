import itertools
from copy import deepcopy
from itertools import product
matrix = [[0]*8]
for _ in range(5):
    matrix.append([0] + list(map(int, input().split())) + [0])
matrix.append([0]*8)
dx = [0, 0, 0, 1]
dy = [-1, 0, 1, 0]

for i in itertools.product([0, 1], repeat=6):
    ans = []
    temp_matrix = deepcopy(matrix)
    first_line = list(i)
    ans.append(first_line)
    for j in range(6):
        if first_line[j] == 1:
            for k in range(4):
                temp_matrix[1+dx[k]][j+1+dy[k]] = abs(temp_matrix[1+dx[k]][j+1+dy[k]] - 1)
    ans.append(temp_matrix[1][1:7])
    for _ in range(4):
        for j in range(6):
            if ans[-1][j] == 1:
                for k in range(4):
                    temp_matrix[len(ans) + dx[k]][j + 1 + dy[k]] = abs(temp_matrix[len(ans) + dx[k]][j + 1 + dy[k]] - 1)
        ans.append(temp_matrix[len(ans)][1:7])
    if ans[-1] == [0,0,0,0,0,0]:
        for j in range(5):
            print(" ".join(map(str, ans[j])))
        break
