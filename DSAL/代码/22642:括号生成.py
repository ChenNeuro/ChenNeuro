ans = set()
n = int(input())


def bfs(n):
    queue = [(1,0,"(")]
    while queue:
        l, r, char = queue.pop()
        if l < r or l > n:
            continue
        elif l == r == n:
            ans.add(char)
        else:
            queue.append((l+1,r,char+"("))
            queue.append((l,r+1,char+")"))


bfs(n)
lst = list(ans)
lst.sort()
for i in lst:
    print("".join(i))
