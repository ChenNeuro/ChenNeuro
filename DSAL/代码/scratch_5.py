ans = []


def queen_dfs(A, cur=0):  # 考虑放第cur行的皇后
    if cur == len(A):  # 如果已经放了n个皇后，一组新的解产生了
        ans.append(''.join([str(x) for x in A]))  # 注意避免浅拷贝
        return

    for col in range(len(A)):  # 将当前皇后逐一放置在不同的列，每列对应一组解
        for row in range(cur):  # 逐一判定，与前面的皇后是否冲突
            # 因为预先确定所有皇后一定不在同一行，所以只需要检查是否同列，或者在同一斜线上
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:  # 若都不冲突
            A[cur] = col  # 放置新皇后，在cur行，col列
            queen_dfs(A, cur + 1)  # 对下一个皇后位置进行递归

N = int(input())
queen_dfs([None] * N)
ans.sort()
if ans:
    for _ in ans:
        print(" ".join(str(j) for j in _))
else:
    print("NO ANSWER")