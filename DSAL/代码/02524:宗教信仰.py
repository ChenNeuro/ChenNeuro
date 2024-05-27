def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

case = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = list(range(n+1))
    for _ in range(m):
        i, j = map(int, input().split())
        union(i, j)
    religions = len(set(find(i) for i in range(1, n+1)))
    case += 1
    print("Case %d: %d" % (case, religions))