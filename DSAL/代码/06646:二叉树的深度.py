class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def maxDepth(self):
        if self is None:  # 如果是空树，返回0
            return 0
        else:  # 否则递归计算左右子树的最大深度
            left_depth = self.left.maxDepth() if self.left else 0
            right_depth = self.right.maxDepth() if self.right else 0
            return max(left_depth, right_depth) + 1  # 返回左右子树的最大深度之中的较大者加1

    def countleaf(self):
        if self is None:  # 如果是空树，返回0
            return 0
        if self.left is None and self.right is None:  # 如果是叶子节点，返回1
            return 1
        else:  # 否则递归计算左右子树的叶子节点数
            left_leaf = self.left.countleaf() if self.left else 0
            right_leaf = self.right.countleaf() if self.right else 0
        return left_leaf + right_leaf  # 返回左右子树的叶子节点数之和

    def root(self):  # 寻找根节点
        parent_node = set(nodes.values())  # 用集合存储所有节点
        for node in nodes.values():  # 遍历所有节点
            if node.left:  # 如果该节点有左子节点，从集合中删除
                parent_node.discard(node.left)
            if node.right:  # 如果该节点有右子节点，从集合中删除
                parent_node.discard(node.right)
        return parent_node.pop().value  # 返回集合中剩下的唯一节点的值


n = int(input())
nodes = {i: BinaryTree(i) for i in range(1, n+1)}  # 创建n个节点

for i in range(1, n+1):
    l, r = map(int, input().split())
    if l != -1:
        nodes[i].left = nodes[l]
    if r != -1:
        nodes[i].right = nodes[r]
x = nodes[1].root()
print(nodes[x].maxDepth())
# print(nodes[x].maxDepth()-1, nodes[x].countleaf())
