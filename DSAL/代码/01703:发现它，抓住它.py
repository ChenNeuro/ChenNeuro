class DisjSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.dist = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            px = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.dist[x] ^= self.dist[px]
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.dist[px] = self.dist[x] ^ self.dist[y] ^ 1
        else:
            self.parent[py] = px
            self.dist[py] = self.dist[x] ^ self.dist[y] ^ 1
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ds = DisjSet(N+1)
    for _ in range(M):
        op, a, b = input().split()
        a, b = int(a), int(b)
        if op == 'D':
            ds.union(a, b)
        else:
            if ds.find(a) != ds.find(b):
                print("Not sure yet.")
            else:
                print("In the same gang." if ds.dist[a] == ds.dist[b] else "In different gangs.")