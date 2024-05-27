class DisjSet:
    def __init__(self, n):
        self.rank = [1] * (n+1)
        self.parent = [(i) for i in range(n+1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
            return False
        return True


while True:
    try:
        n, m = map(int, input().split())
        ds = DisjSet(n)
        for i in range(m):
            x, y = map(int, input().split())
            if ds.union(x, y):
                print("Yes")
            else:
                print("No")

        ds.parent[1:] = [ds.find(i) for i in ds.parent[1:]]
        print(len(set(ds.parent[1:])))
        print(" ".join(str(i) for i in sorted(list(set(ds.parent[1:])))))

    except EOFError:
        break
