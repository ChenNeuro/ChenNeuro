class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.weights = [0] * n

    def find(self, x):
        # Find the root of the set in which element x belongs
        if self.parent[x] != x:
            # Path compression: Make the parent of x the root of its set
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Perform union of two sets
        x_root, y_root = self.find(x), self.find(y)

        if x_root == y_root:
            return
        # Attach smaller rank tree under root of higher rank tree
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.weights[y_root] += self.weights[x_root]
        else:
            self.parent[y_root] = x_root
            self.weights[x_root] += self.weights[y_root]
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1


n, m = map(int, input().split())
ds = DisjSet(n)
weights = list(map(int, input().split()))
ds.weights = weights.copy()
for i in range(m):
    u, v = map(int, input().split())
    ds.union(u, v)

max_weight = max(ds.weights)
print(max_weight)