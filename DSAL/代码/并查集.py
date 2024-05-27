class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

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
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1



# 示例用法
A = DisjSet(5)
B = DisjSet(5)

A.union(0, 1)
A.union(2, 3)

print(A.rank)    # 输出: [2, 1, 2, 1, 1]
print(A.parent)  # 输出: [0, 0, 2, 2, 4]
print(B.rank)    # 输出: [1, 1, 1, 1, 1]
print(B.parent)  # 输出: [0, 1, 2, 3, 4]