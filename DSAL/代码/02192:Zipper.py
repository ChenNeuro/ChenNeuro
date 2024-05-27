def can_form(A, B, C):
    lenA, lenB, lenC = len(A), len(B), len(C)
    if lenA + lenB != lenC:
        return False

    dp = [[False] * (lenB + 1) for _ in range(lenA + 1)]
    dp[0][0] = True

    for i in range(lenA + 1):
        for j in range(lenB + 1):
            if i > 0 and A[i - 1] == C[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if j > 0 and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]

    return dp[lenA][lenB]


def bfs(A, B, C):
    lenA, lenB, lenC = len(A), len(B), len(C)
    if lenA + lenB != lenC:
        return False

    queue = [(0, 0)]
    visited = set((0, 0))

    while queue:
        a, b = queue.pop()
        if a + b == lenC:
            return True

        if a < lenA and A[a] == C[a + b] and (a + 1, b) not in visited:
            queue.append((a + 1, b))
            visited.add((a + 1, b))
        if b < lenB and B[b] == C[a + b] and (a, b + 1) not in visited:
            queue.append((a, b + 1))
            visited.add((a, b + 1))

    return False


n = int(input())
for i in range(1, n + 1):
    A, B, C = input().split()
    if bfs(A, B, C):
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")


