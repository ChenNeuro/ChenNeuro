N = int(input())
block = [set(input()) for _ in range(4)]


def dfs(word):
    if len(word) == 0:
        return True
    for i in range(4):
        if not v[i]:
            if word[0] in block[i]:
                v[i] = True

                if dfs(word[1:]):
                    return True
                v[i] = False

    return False


for i in range(N):
    s = input()
    n = len(s)
    v = [False] * 4
    if dfs(s):
        print("YES")
    else:
        print("NO")